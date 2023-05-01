from django.db import models

class Base(models.Model):
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class UserModel(Base):
    username = models.CharField(max_length=10, blank=False)
    password = models.CharField(max_length=20, blank=False)