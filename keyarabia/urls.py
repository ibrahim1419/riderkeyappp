from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetConfirmView,
    PasswordResetView,
)
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import TokenVerifyView

from common.permissions import IsAdmin, IsStaff

schema_view = get_schema_view(
    openapi.Info(
        title="Keyarabia API",
        default_version="v1",
    ),
    public=False,
    permission_classes=[IsAdmin | IsStaff],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # Authentication views
    path(
        "auth/password/reset/confirm/<str:uidb64>/<str:token>",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path("auth/password/reset/", PasswordResetView.as_view(), name="rest_password_reset"),
    path("auth/password/reset/confirm/", PasswordResetConfirmView.as_view(), name="rest_password_reset_confirm"),
    path("auth/login/", LoginView.as_view(), name="rest_login"),
    path("auth/logout/", LogoutView.as_view(), name="rest_logout"),
    path("auth/password/change/", PasswordChangeView.as_view(), name="rest_password_change"),
    path("auth/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("auth/token/refresh/", get_refresh_view().as_view(), name="token_refresh"),
    # Users API urls
    path("", include("users.api.urls")),
    # Employees API urls
    path("", include("employees.api.urls")),
    # Documentation
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]
