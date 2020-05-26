from django.shortcuts import render
from django.http import HttpResponse
from .models import JobPost

# Create your views here.
def home_view(request):
    #Getting the job posts
    job_post = JobPost.objects.all()
    context = {
        'job':job_post

    }
    return render(request, 'layout/index.html',{'context':context})