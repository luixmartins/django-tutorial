from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=30)
    birthday = models.DateField("Date of Birth")

class AddressUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    number = models.IntegerField()
    district = models.CharField(max_length=50)


