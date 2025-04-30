from reviews.views import RegisterView, ChangePasswordView
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from book_reviews.views import BookViewSet, ReviewViewSet

# ل Swagger و Redoc
from rest_framework.authtoken import views as drf_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

# إعداد الراوتر
router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'reviews', ReviewViewSet)

# إعداد التوثيق Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Book Review API",
        default_version='v1',
        description="API for managing books and reviews",
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    path('api-token-auth/', drf_views.obtain_auth_token),  # إصدار التوكن ✅
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger ✅
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # Redoc ✅
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),

]
