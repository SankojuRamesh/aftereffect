"""
URL configuration for AF project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from afmanager import views
# urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

 
 
from rest_framework import routers
from afmanager.views import LayerViewSet, ProjectViewset, CompositViewSet

 
from django.conf.urls.static import static
from django.conf import settings
router = DefaultRouter()
router.register(r'projects', ProjectViewset)

router.register(r'composit', CompositViewSet)

router.register(r'pdata', LayerViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="SD SERVICE ",
        default_version='v1',
        description="API documentation for SDSERVICE App",
        terms_of_service=" ",
        contact=openapi.Contact(email="ramesh@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

swagger_info = openapi.Info(
    title="SD SRVICE",
    default_version='v1',
    description="API documentation for SD SRVICE App",
    terms_of_service="https://www.example.com/terms/",
    contact=openapi.Contact(email="contact@example.com"),
    license=openapi.License(name="MIT License"),
)

 
urlpatterns = [
    path('admin/', admin.site.urls),     
     path('projects/', include(router.urls)),
    path('', views.Home),
    path('composit', views.Composits),
    path("new", views.newproject),
     path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
