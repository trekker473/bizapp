from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
# Create your models here.

class Org(models.Model):
    orgName = models.CharField(max_length=50)
    lastUpdated = models.DateTimeField()
    description = models.TextField()
    createdDateTime = models.DateTimeField()

    def __str__(self):
        return entityName

class Person(models.Model):
    person = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    org = models.ForeignKey('Org', on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField()
    lastUpdated = models.DateTimeField()

    def __str__(self):
        return f'(self.person.user.username)'

class PhoneNumber(models.Model):
    countryCode = models.IntegerField()
    areaCode = models.IntegerField()
    phoneNumber = models.IntegerField()
    ext = models.IntegerField()
    type = models.CharField(max_length=20)
    ownerPerson = models.ManyToManyField(Person)
    ownerOrg = models.ManyToManyField(Org)


class Address(models.Model):
    address1 = models.CharField(max_length=40)
    address2 = models.CharField(max_length=40)
    stateOrProvince = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=15)
    country = models.CharField(max_length=20)


class Email(models.Model):
    ownerPerson = models.ManyToManyField(Person)
    ownerOrg = models.ManyToManyField(Org)
    type = models.CharField(max_length=40)
    emailAddress = models.EmailField()


class Note(models.Model):
    createdDateTime = models.DateTimeField()
    lastUpdated = models.DateTimeField()
    content = models.TextField()
    createdBy = models.ForeignKey(Person, on_delete=models.CASCADE)
