from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Etablissement


class User(AbstractUser):
    etablissement = models.ForeignKey(Etablissement, null=True, blank=True, on_delete=models.SET_NULL)