from django.shortcuts import render, HttpResponse
import git
import subprocess

# Create your views here.
def home(request):
    # return HttpResponse("Hello World!")
    return render(request, 'base.html')

def update_webhook(request):
    # function to handle webhook push from github
    # one more comment added
    repo = git.Repo('/home/tanishashankpal/myprofile/myapp')
    repo.remotes.origin.pull()
    # python manage.py collectstatic --noinput
    subprocess.run(["cd", "/home/tanishashankpal/myprofile"])
    subprocess.run(["python", "manage.py", "collectstatic", "--noinput"])
    return HttpResponse("Hello World!")