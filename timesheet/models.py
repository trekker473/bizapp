from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

#class Timesheet(models.Model):
#    employee = models.ForeignKey(User, on_delete=models.PROTECT)


#class TimeEntry(models.Model):
#    timesheet = models.ForeignKey(Timesheet, on_delete=models.PROTECT)
    #job = (list of jobs from job)
#    timeIn = models.DateTimeField(default=timezone.now)
#    timeOut = models.DateTimeField(default=timezone.now)
    #Note = (list of note entries)


#class job(models.Model):
#    employee = user
#    paytypes = (dictionary paytype_name : rate)
#    start_date = date
#    end_date = date


class timeNote(models.Model):
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)#Should be changed to PROTECT
    createdDateTime = models.DateTimeField(auto_now_add=True)
    #readBy = list of users
    content = models.TextField()
