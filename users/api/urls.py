from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register("users", viewset=views.UserViewSet)

urlpatterns = [
    # User routes
    path("users/", views.UserViewSet.as_view({"get": "list"})),
    path(
        "users/<int:pk>/",
        views.UserViewSet.as_view(
            {"get": "retrieve", "delete": "destroy", "put": "update", "patch": "partial_update"}
        ),
    ),
    # Auth routes
    path("auth/register/", views.UserViewSet.as_view({"post": "create"})),
    path("auth/activateemail/<str:uidb64>/<str:token>/", views.EmailActivationView.as_view(), name="activate_email"),
    path("auth/activateemail/", views.ResendEmailActivationView.as_view()),
]
