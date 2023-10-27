from django.db import models

class Style(models.Model):
    style_id = models.CharField(max_length=100, primary_key=True)
    category = models.CharField(max_length=100)

class Product(models.Model):
    asin = models.CharField(max_length=100, primary_key=True)
    sku = models.CharField(max_length=100)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    stock = models.DecimalField(max_digits=10, decimal_places=1)

class City(models.Model):
    zip_code = models.BigIntegerField(verbose_name='zip code', primary_key=True)
    city_name = models.CharField(max_length=100, verbose_name='city name')
    state = models.CharField(max_length=100, verbose_name='state')
    
class Order(models.Model):
    orderid = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=100)
    fulfilment = models.CharField(max_length=100)
    saleschannel = models.CharField(max_length=100)
    shipservicelevel = models.CharField(max_length=100)
    asin = models.ForeignKey(Product, on_delete=models.CASCADE)
    courierstatus = models.CharField(max_length=100)
    qty = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    zip_code = models.ForeignKey(City, on_delete=models.CASCADE)
    b2b = models.BooleanField()

    def __str__(self):
        return f"Order {self.orderid}: {self.date} - {self.status}"

class Denormalized(models.Model):
    date = models.DateField(auto_now=False)  
    status = models.CharField(max_length=100, default='') 
    is_weekend = models.BooleanField(verbose_name='is weekend', default=False)
    fulfilment = models.CharField(max_length=100, default='') 
    saleschannel = models.CharField(max_length=100, default='') 
    shipservicelevel = models.CharField(max_length=100, default='') 
    courierstatus = models.CharField(max_length=100, default='')  
    qty = models.IntegerField(default=0)  
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    b2b = models.BooleanField(default=False)  
    stock = models.IntegerField(default=0)  
    shipcity = models.CharField(max_length=100, default='') 
    shipstate = models.CharField(max_length=100, default='')  
    color = models.CharField(max_length=100, default='')  
    size = models.CharField(max_length=100, default='')  
    category = models.CharField(max_length=100, default='')  

    def __str__(self):
        return f"Denormalized {self.id}: {self.date} - {self.status}"

