from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
import uuid
# Create your models here.

class Org(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    orgName = models.CharField(max_length=50)
    description = models.TextField()
    createdDateTime = models.DateTimeField()

    def __str__(self):
        return entityName

class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(Profile, on_delete=models.CASCADE)
    org = models.ForeignKey(Org, on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField()

    def __str__(self):
        return f'(self.person.user.username)'

class PhoneNumber(models.Model):
    countryCode = models.IntegerField()
    areaCode = models.IntegerField()
    phoneNumber = models.IntegerField()
    ext = models.IntegerField()
    description = models.CharField(max_length=40)
    ownerUUID = models.CharField(max_length=32)#maybe many to many


class Address(models.Model):
    address1 = models.CharField(max_length=40)
    address2 = models.CharField(max_length=40)
    stateOrProvince = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=15)
    country = models.CharField(max_length=20)


class Email(models.Model):
    ownerPerson = models.ForeignKey(Person, on_delete=models.CASCADE)
    ownerOrg = models.ForeignKey(Org, on_delete=models.CASCADE)
    type = models.CharField(max_length=40)
    emailAddress = models.EmailField()


class Note(models.Model):
    objectID = models.CharField(max_length=32)
    createdDateTime = models.DateTimeField()
    content = models.TextField()
    createdBy = models.ForeignKey(Person, on_delete=models.CASCADE)

class Employee(models.Model):
    employee = models.ForeignKey(Person, on_delete=models.CASCADE)
    employer = models.ForeignKey(Org, on_delete=models.CASCADE)
    #client = models.ForeignKey(Org, on_delete=models.CASCADE)
    payRate = models.IntegerField()
    billRate = models.IntegerField()


class Update(models.Model):
    updateAuthor = models.ForeignKey(User, on_delete=models.CASCADE)
    itemPrimaryKey = models.IntegerField()
    updateDateTime = models.DateTimeField(auto_now_add=True)
    updateDetails = models.TextField()
