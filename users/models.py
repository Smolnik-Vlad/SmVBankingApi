from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from users.constants import PASSPORT_SERIE
from users.managers import UserProfileManager


# Create your models here.
class UserProfile(AbstractUser):
    objects = UserProfileManager()
    username = models.SlugField(max_length=30, null=True, blank=True, default=None, unique=False)
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    patronymic = models.CharField(max_length=30, null=False, blank=True, default='')
    passport_series = models.CharField(choices=PASSPORT_SERIE, max_length=2, null=False, blank=False)
    passport_id = models.CharField(max_length=7, null=False, blank=False, unique=True)
    email = models.EmailField(null=False, blank=False, unique=True)
    last_login = models.DateTimeField(_("last login"), blank=True, null=True, auto_now=True)
    telephone_number = models.CharField(max_length=20, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "patronymic", "passport_series", "passport_id", "password"]

    def get_full_name(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    def save(self, *args, **kwargs):
        slug_data = self.email.split('@')[0]
        self.username = slugify(slug_data)
        return super().save(*args, **kwargs)

    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     related_name='common_users',
    #     verbose_name='groups',
    #     blank=True,
    #     help_text='The groups this user belongs to.',
    #     related_query_name='common_user'
    # )
    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     related_name='common_users',
    #     verbose_name='user permissions',
    #     blank=True,
    #     help_text='Specific permissions for this user.',
    #     related_query_name='common_user'
    # )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'profile users'
        verbose_name_plural = 'profile user'


class Client(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='client')
    work_place = models.CharField(max_length=100, null=True, blank=True)
    user_info = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'clients'
        verbose_name_plural = 'client'

    def __str__(self):
        return self.user.username
