from django.shortcuts import render,HttpResponse

# Create your views here.
def home(requests):
    first_name = "Adam"
    age = 20
    return render(requests,'home.html',{'name':first_name , 'age' : age})

def login(requests):
    return render(requests,'login.html')

def signup(requests):
    return render(requests,'signup.html')

def add(requests):
    val1 = int(requests.POST['num1'])
    val2 = int(requests.POST['num2'])
    val3 = val1 + val2
    return render(requests,'add.html',{'result' : val3})

def register(requests):
    return render(requests,'register.html')