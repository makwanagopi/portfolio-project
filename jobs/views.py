from django.shortcuts import render
from .models import Job
def home(request):
	jobs = Job.objects
	return render(request,'home.html',{'jobs':jobs})
# Create your views here.
