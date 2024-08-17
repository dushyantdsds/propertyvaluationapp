from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_email = models.EmailField(unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)  # Allow null and blank values
    phone = models.CharField(max_length=15, null=True, blank=True)
    role = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        self.user_email = self.user.email
        super().save(*args, **kwargs)
