from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from rest_framework import viewsets
from .serializers import CourseSerializer

# Create your views here.

def welcome(request):
    return render(request,'welcome_courses.html')
    
def courses(request):
    courses = Course.objects.all()
    
    context ={
        'courses':courses
    }
    return render(request,'listing_courses.html',context)
    
     
#viewSets define the view behaviour
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer