from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import (Employee, Payslip, Attendance, User)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user


class SignInSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect credentials")


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employee
        fields = ['id', 'name', 'designation', 'salary', 'pf_rate', 'user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        employee = Employee.objects.create(user=user, **validated_data)
        return employee


class PayslipSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()

    class Meta:
        model = Payslip
        fields = ['id', 'employee', 'month', 'basic_salary', 'pf_deduction', 'total_salary']

    def create(self, validated_data):
        employee_data = validated_data.pop('employee')
        employee = Employee.objects.create(**employee_data)
        payslip = Payslip.objects.create(employee=employee, **validated_data)
        return payslip


 