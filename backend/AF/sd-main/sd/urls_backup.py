from django.urls import include, path
from rest_framework.routers import DefaultRouter

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin

router = DefaultRouter()
# router.register('users', UserViewSet)
# router.register('employees', EmployeeViewSet)
# router.register('payslips', PayslipViewSet)
# router.register('attendance', AttendanceViewSet)

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
   # path('api/signin/', SignInView.as_view(), name='signin'),
   path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/user/', include('usermanager.urls')),
    path('api/employee/', include('employeemanager.urls')),
    path('api/salary/', include('salarymanager.urls')),
    path('api/company/', include('companymanager.urls')),
    path('api/attendance/', include('attendencemanager.urls')),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
