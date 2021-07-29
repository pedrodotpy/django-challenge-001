from django.contrib.auth.models import AbstractUser

from challenge.helpers import BaseModelMixin


class User(BaseModelMixin, AbstractUser):
    created_at = None  # AbstractUser already has a similar field called date_joined
