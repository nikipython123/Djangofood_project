from django.db import models

# Create your models here.
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
