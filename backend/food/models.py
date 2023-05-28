from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Recipe(models.Model):
    class Meta:
        db_table = 'recipe'

    author = models.CharField(max_length=16)
