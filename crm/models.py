from django.db import models

# Create your models here.

class Company(models.Model):
    companyName =

    def __str__(self):
        return companyName

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'(self.user.username)'

class PhoneNumber(models.Model):

class Address(models.Model):

class Email(models.Model):

class Note(models.Model):
