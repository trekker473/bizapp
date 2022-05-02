from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
# Create your models here.

class Entity(models.Model):
    entityName = models.CharField()
    lastUpdated = models.DateTimeField()
    description = models.TextField()
    createdDateTime = models.DateTimeField()

    def __str__(self):
        return entityName

class Person(models.Model):
    person = models.ForeignKey('Profile', on_delete=models.CASCADE)
    entity = models.ForeignKey('Entity', on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField()
    lastUpdated = models.DateTimeField()

    def __str__(self):
        return f'(self.person.user.username)'

class PhoneNumber(models.Model):
    countryCode = models.IntergerField()
    areaCode = models.IntergerField()
    phoneNumber = models.IntergerField()
    ext = models.IntergerField()
    type = models.CharField()
    personOwner = models.ManyToManyField()
    entityOwner = models.ManyToManyField()


class Address(models.Model):
    address1 = models.CharField()
    address2 = models.CharField()
    stateOrProvince = models.CharField()
    zipcode = models.CharField()
    country = models.CharField()


class Email(models.Model):
    personOwner = models.ManyToManyField()
    entityOwner = models.ManyToManyField()
    type = models.CharField()
    emailAddress = models.EmailField()


class Note(models.Model):
    createdDateTime = models.DateTimeField()
    lastUpdated = models.DateTimeField()
    content = models.TextField()
    createdBy = models.ForeignKey()
