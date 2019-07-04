from django.db import models
from django.contrib.auth.models import User



class perfil(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    avatar = models.ImageField(upload_to='images/avatar')
    profesion = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username 
    