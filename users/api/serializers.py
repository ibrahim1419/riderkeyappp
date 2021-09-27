from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name", "email", "country", "password")
        extra_kwargs = {"password": {"write_only": True}}


class UsersStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "name",
            "country",
            "email",
            "password",
            "password2",
        )
        extra_kwargs = {"name": {"required": True}}

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            name=validated_data["name"], email=validated_data["email"], country=validated_data["country"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
