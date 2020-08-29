from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import CustomUserManager

USER_TYPE_CHOICES = (
    (0, 'Investor'),
    (1, 'Borrower'),
)


class CustomUser(AbstractUser):
    email = models.EmailField(('email address'), unique=True, null=False, blank=False)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=0)
    score = models.PositiveSmallIntegerField(default=0)

    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)
