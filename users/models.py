from concurrent.futures.process import _python_exit
import email
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    residence = models.CharField(null=True, blank=True, max_length=200)
    skills = models.TextField()
    image = models.ImageField(default='default_user.jpg', upload_to='profile_pics/')
    email = models.EmailField()
    phone = models.CharField(null=True, blank=True, max_length=20)
    bio = models.TextField(null=True, blank=True, max_length=200)

    def __str__(self):
        return f'{self.user.username} Profile'

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
