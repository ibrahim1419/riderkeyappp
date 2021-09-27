from django.contrib.auth.models import AbstractBaseUser
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class Users(AbstractBaseUser):
    TYPE_CHOICES = (("admin", _("Admin")), ("staff", _("Staff")), ("employee", _("Employee")))
    COUNTRY_CHOICES = (("bahrain", _("Bahrain")), ("erbil", _("Erbil")), ("dubai", ("Dubai")), ("iraq", _("Iraq")))

    last_login = None
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(_("name"), max_length=255)
    email = models.EmailField(_("email address"), unique=True, max_length=255)
    type = models.CharField(_("type"), choices=TYPE_CHOICES, max_length=255, default="employee")
    country = models.CharField(_("country"), choices=COUNTRY_CHOICES, max_length=128)
    remember_token = models.CharField(_("remember token"), max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(_("date joined"), auto_now_add=True, null=True)
    updated_at = models.DateTimeField(_("last update"), auto_now=True, null=True)
    is_active = models.BooleanField(_("is active"), default=True)
    email_verified_at = models.DateTimeField(_("email verified at"), blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "country"]

    objects = UserManager()

    class Meta:
        db_table = "users"
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_name(self):
        """Return the name for the user."""
        return self.name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.email
