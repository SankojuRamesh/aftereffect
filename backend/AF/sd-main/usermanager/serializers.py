# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework_simplejwt import serializers as jwt_serializers
from rest_framework_simplejwt.tokens import RefreshToken
from . import models

User = get_user_model()


class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserRole
        fields = '__all__'

class CreateUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        write_only=True, required=True, min_length=5, max_length=24
    )
    role = UserRoleSerializer(source='roles', read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
            'confirm_password',
            'name',
            'address',
            'contact',
            
            'roles',
            'role',
        )
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 5, 'max_length': 24},
            'roles': {'write_only': True, 'required': True},
        }

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError({'password': _("Passwords not matching!")})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer to view all Users
    """

    roles = serializers.CharField(source='get_roles')

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'address', 'contact', 'avatar', 'roles', 'is_active')
        read_only_fields = ('email', 'is_active')

    def update(self, instance, validated_data):
        role_name = validated_data.pop('get_roles', None)
        user = super().update(instance, validated_data)

        # Role must be either Supplier/SpotSupplier
        role = account.models.UserRole.objects.filter(
            name__in=['Admin', 'Superadmin'], name__iexact=role_name
        ).first()
        if role:
            user.roles = role
            user.save()

        return user

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.update(instance.app_modules)
        return representation

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserRole
        fields = '__all__'


class SignInSerializer(jwt_serializers.TokenObtainPairSerializer):
    """
    Return Access, Refresh tokens along with User data
    """

    def validate(self, attrs):
        data = super().validate(attrs)
        return data
        # user = UserSerializer(self.user, context=self.context).data
        # data.update(user)
        # return data




class UserReadOnlySerializer(serializers.ModelSerializer):
    """
    Return User data.
    """

    role = serializers.CharField(source='get_roles')

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'role')
