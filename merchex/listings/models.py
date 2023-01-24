from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models, transaction
from django.conf import settings


class CustomUserManager(BaseUserManager):
    """
    Custom user manager is necessary for custom user with custom fields (notably email as username) to work.
    """
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')
        with transaction.atomic():
            user = self.model(email=self.normalize_email(email), **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user, notably for email as username.
    Declared in settings.py
    """
    email = models.EmailField(
        max_length=255, unique=True, verbose_name='email address',
        error_messages={'unique':'A user with this email already exists.'})
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        return self.is_superuser

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

class Band(models.Model):
    name = models.fields.CharField(max_length=100)

