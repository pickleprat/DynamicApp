from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def products(request):
    return render(request, "home/products.html")

def calender(request):
    return render(request, "calendar/index.html")

def loginpage(request):
    return render(request, "loginpage/loginpage.html")