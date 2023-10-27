from django.contrib import admin
from .models import Style, Product

# Register your models here.
admin.site.register([
    Product, 
    Style, 
])