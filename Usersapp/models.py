from django.db import models

# Create your models here.
class UsersModel(models.Model):
  name = models.CharField(max_length=32)
  phone = models.CharField(max_length=13,unique=True,null=True)
  created_at = models.DateTimeField(auto_now_add=True,editable=True,blank=True)
  otp = models.CharField(max_length=4,null=True)
  email = models.EmailField(unique=True)
  age = models.IntegerField()


  def __str__(self):
    return self.name