from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    age = models.PositiveBigIntegerField(null=True, blank = True)

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), null=True, on_delete=models.CASCADE,  related_name="profile")
    profile_image = models.ImageField(default='', upload_to='static/images/', null=True, blank=True)
    dob = models.DateField(null=False, blank = False, default='')
    address = models.CharField(max_length=200, default='')
    phone = models.IntegerField(default=0)
    email = models.EmailField(default='')

    def __str__(self):
        return str(self.user)