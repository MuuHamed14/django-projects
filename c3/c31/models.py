from django.db import models
from django.contrib.auth.models import User
class staff(models.Model):
    fullname = models.CharField(max_length = 100)
    email = models.EmailField(null = True)
    age = models.IntegerField()
    birthday = models.DateField( null = True)
    fr = models.CharField(null = True, max_length = 100)
    department = models.CharField(max_length = 100)
    def __str__(self):
     return self.fullname
class info(models.Model):
    username = models.ForeignKey(User,on_delete = models.CASCADE)
    jobs = models.CharField(max_length = 100)
    lang = models.CharField(max_length = 100)
    number = models.IntegerField()
class pic(models.Model):
    name = models.CharField(max_length = 100)
    img = models.ImageField(upload_to = 'c31/static/c31/images/')