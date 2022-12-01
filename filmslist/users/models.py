from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='6d0707b4fecda5e1f930d4a445b1afa9.jpeg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'