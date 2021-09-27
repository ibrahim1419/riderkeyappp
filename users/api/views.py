from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from common.permissions import IsAdmin, IsOwner, IsStaff

from ..tokens import account_activation_token
from ..utils import send_activation_email
from .serializers import UserRegisterSerializer, UsersSerializer, UsersStaffSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "pk"

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [AllowAny]
        elif self.action == "retrieve":
            permission_classes = [IsAdmin | IsStaff | IsOwner]
        else:
            permission_classes = [IsAdmin | IsStaff]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == "create":
            return UserRegisterSerializer

        if self.request.user.type.lower() == "employee":
            return UsersSerializer
        return UsersStaffSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        send_activation_email(user)


class EmailActivationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.email_verified_at = timezone.now()
            user.save()
            return Response({"message": "Email activated successfully"})
        else:
            return Response({"token": "Invalid value"})


class ResendEmailActivationView(APIView):
    permission_classes = [IsOwner]

    def post(self, request):
        send_activation_email(self.request.user)
        return Response({"message": "Activation email sent"})
