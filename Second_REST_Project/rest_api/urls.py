from . models import Student
from django.conf import urls
from django.urls import path
from . views import StudentList

urlpatterns = [
    path('students', StudentList.as_view())
]