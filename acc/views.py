
from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect

# Create your views here.

def acc(requests):
    return render(requests,'accounts.html')


def login(requests):
    return render(requests,'log.html')

def signup(requests):
    if requests.method == 'POST':
        Firstname=requests.POST['first_name']
        lastname=requests.POST['last_name']
        Email=requests.POST['email']
        Username=requests.POST['user_name']
        Password=requests.POST['password']

        user = User.objects.create_user(first_name=Firstname,last_name=lastname,email=Email,password=Password,user_name=Username)
        return redirect('/')
    else:
        return render(requests,'sig.html')