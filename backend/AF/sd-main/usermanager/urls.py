# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
 
from  . import views

app_name = 'user'
 
urlpatterns = [
    path('roles/', views.UserRoleListView.as_view(), name='user_roles'),
    path('sign-in/', views.SignInView.as_view(), name='sign_in'),
    #path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
]