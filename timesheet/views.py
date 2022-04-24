from django.shortcuts import render
from django.http import HttpResponse
from .models import timeNote

# Create your views here.

notes = [
    {
        'subject' : 'Getting Started',
        'content': 'Add your hours for the given days',
        'date_posted': 'August 3, 2019'
    },
    {
        'subject' : 'Recording Lunch Breaks',
        'content': 'By default, each day only starts with one time in and one time out field. Add your time for the pre-lunch period, then click on "Add more time" and enter your post-lunch hours',
        'date_posted': 'August 3, 2019'
    },
]


def home(request):
    return render(request, 'timesheet/home.html')

def help(request):
    context = {
        'notes': timeNote.objects.all()
    }
    return render(request,'timesheet/help.html', context)
