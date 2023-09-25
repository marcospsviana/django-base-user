import re

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def _create_user(
        self, email, password, is_staff, is_superuser, **extra_fields
    ):
        
        now = timezone.now()
        email = self.normalize_email(email)
        username = str(email).split('@')[0]
        print(f'Username in create {username} e email : {email}')
        user = self.model(
            username=username,
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        
        return self._create_user(
            email, password, False, False, **extra_fields
        )

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(
            email, password, True, True, **extra_fields
        )
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), max_length=255, unique=True)
    password = models.CharField(verbose_name='password', max_length=15)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(            'Designates whether the user can log into this admin site.'
        ),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. \
        Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_trusty = models.BooleanField(
        _('trusty'),
        default=False,
        help_text=_('Designates whether this user has confirmed his account.'),
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_username(self):
        return self.email.split('@')[0]

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])
