from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#user=models.ForeignKey(tABLEnAME,on_delete=models.CASCADE)
class userfeedback(models.Model):
    username=models.CharField(max_length=20)
    rating=models.IntegerField()
    feedback=models.TextField()
    created_at=models.DateTimeField()

class FoodInsert(models.Model):
    Food_id=models.CharField(max_length=20)
    Customer_name=models.CharField(max_length=20)
    Product_name=models.CharField(max_length=20)
    Product_quntity=models.CharField(max_length=20)
    Product_prize=models.FloatField()
    address=models.TextField()
    Date_time=models.DateTimeField()

class ViewRegister(models.Model):
    First_name=models.CharField(max_length=30)
    Last_name=models.CharField(max_length=30)
    user_name=models.CharField(max_length=30)
    password=models.CharField(max_length=20)

class AddtoCart(models.Model):
    pro_name=models.CharField(max_length=20)
    pro_image=models.ImageField(upload_to='uploads/cover_page/')
    pro_quntity=models.CharField(max_length=20)
    pro_prize=models.FloatField()

class Buyproduct(models.Model):
    cus_pro=models.CharField(max_length=20)
    quntity=models.CharField(max_length=20)
    add_prize=models.FloatField(default=30)
    cus_add=models.TextField()