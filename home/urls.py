from django.urls import path
from .views import home, products, calender, loginpage

urlpatterns = [
    path("", home, name="home"),
    path("products/", products, name="products"), 
    path("calender/", calender, name="calender"), 
    path("loginpage/", loginpage, name="loginpage"), 
]