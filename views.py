from django.shortcuts import render, HttpResponse
import git

# Create your views here.
def home(request):
    # return HttpResponse("Hello World!")
    return render(request, 'base.html')

def update_webhook(request):
    # function to handle webhook push from github
    pass