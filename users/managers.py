from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, name, email, type, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email or not name:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(name=name, email=email, type=type, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, name, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        return self.create_user(name, email, "admin", password, **extra_fields)
