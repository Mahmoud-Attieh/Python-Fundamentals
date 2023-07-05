from django.db import models

class Users (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    age =models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    apdated_at = models.DateTimeField(auto_now=True)
