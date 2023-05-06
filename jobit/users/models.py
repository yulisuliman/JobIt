from datetime import date

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User
from PIL import Image

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    date_of_birth = models.DateTimeField()
    profession = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=50, default='')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,  default='0')

    def __str__(self):
        return self.user.username

    # def save(self, *args, **kwargs):
    #     super(Profile, self).save(*args, **kwargs)
    #
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

