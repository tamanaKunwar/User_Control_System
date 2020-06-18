from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    pass

    def __str__(self):
        return self.name

