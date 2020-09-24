from django.db import models
class student(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    age = models.IntegerField()
    birthday = models.DateField()
    def __str__(self):
        return self.name