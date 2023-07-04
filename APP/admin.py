from django.contrib import admin
from .models import userfeedback,FoodInsert,ViewRegister,AddtoCart,Buyproduct

# Register your models here.
admin.site.register(userfeedback)
admin.site.register(FoodInsert)
admin.site.register(ViewRegister)
admin.site.register(AddtoCart)
admin.site.register(Buyproduct)


