from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='timesheet-home'),
    path('help/', views.help, name='timesheet-help'),
    path('timesheet/', views.timesheet, name='timesheet'),
]
