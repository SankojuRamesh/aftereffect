# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from rest_framework import generics, parsers, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt import views as jwt_views

from . import models, serializers

class SignInView(jwt_views.TokenObtainPairView):
    """
    SignIn Endpoint using email & password
    Response: access & refresh tokens
    """

    serializer_class = serializers.SignInSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


class UserRoleListView(generics.ListAPIView):
    """
    Only Admins can access this API
    """

    queryset = models.UserRole.objects.filter(name__in=['Admin', 'Employee', 'SuperAdmin'])
    serializer_class = serializers.UserRoleSerializer
    permission_classes = [permissions.IsAuthenticated ]

