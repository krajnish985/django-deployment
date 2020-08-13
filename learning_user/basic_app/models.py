from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):

    user =models.OneToOneField(User,on_delete=models.CASCADE)


    portfolio_link=models.URLField(blank=True)
    # blank =True mean not compulsory to provide

    portfolio_image= models.ImageField(upload_to='profile_pics',blank=True)
    # upload_to mean in which folder to be stored
    # since it is user provided good to store to in media folder
    # create a folder in media same name as provided 'profile_pics'

    # ####
    # tO USE ImageField PIP INSTALL PILLOW


    def __str__(self):
        return self.user.username
