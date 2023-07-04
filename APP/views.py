from django.shortcuts import render,redirect
from .models import userfeedback,FoodInsert,ViewRegister,AddtoCart,Buyproduct
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request,'base.html')

def adminloadlogin(request):
    return render(request,'login.html')  

def registerlogin(request):
    return render(request,'registerlogin.html')

def feedback(request):
    return render(request,'feedback.html')

def displayfeed(request):
    feedobj=userfeedback.objects.all()
    return render(request,'viewfeedback.html',{'data':feedobj})

def insertfeedback(request):
    if request.method=='POST':
        vuname=request.POST.get('uname')
        vrate=request.POST.get('rate')
        vfeed=request.POST.get('feed')
        vdt=request.POST.get('dt')
        obj=userfeedback()
        obj.username=vuname
        obj.rating=vrate
        obj.feedback=vfeed
        obj.created_at=vdt
        obj.save()
        return redirect('/')
    
def adminlogin(request):
    if request.method=='POST':
        vuname=request.POST.get('uname')
        vpass=request.POST.get('upass')
        user=auth.authenticate(username=vuname,password=vpass)
        if user is not None:
            auth.login(request,user)
            return redirect('/adminpage')
        else:
            return redirect('/login')
        
def adminpage(request):
    return render(request,'Adminpage.html')

def foodpage(request):
    return render(request,'Addfood.html')

def insertfood(request):
    if request.method=='POST':
        vfid=request.POST.get('fid')
        vcus=request.POST.get('cname')
        vpname=request.POST.get('pname')
        vpquntity=request.POST.get('pq')
        vprize=request.POST.get('prize')
        vadd=request.POST.get('add')
        vdt=request.POST.get('dt')
        obj=FoodInsert()
        obj.Food_id=vfid
        obj.Customer_name=vcus
        obj.Product_name=vpname
        obj.Product_quntity=vpquntity
        obj.Product_prize=vprize
        obj.address=vadd
        obj.Date_time=vdt
        obj.save()
    return redirect('/viewfood')
    
def displayfood(request):
    foodobj=FoodInsert.objects.all()
    return render(request,'viewaddfood.html',{'data':foodobj})

def delFood(request,fid):
    food=FoodInsert.objects.get(id=fid)
    food.delete()
    return redirect('/viewfood')

def editfood(request,fid):
    food=FoodInsert.objects.get(id=fid)
    return render(request,'editfood.html',{'data':food})
 
def updatefood(request,fid):
    obj=FoodInsert.objects.get(id=fid)
    if request.method=='POST':
        vfid=request.POST.get('fid')
        vcus=request.POST.get('cname')
        vpname=request.POST.get('pname')
        vpquntity=request.POST.get('pq')
        vprize=request.POST.get('prize')
        vadd=request.POST.get('add')
        vdt=request.POST.get('dt')
        obj=FoodInsert()
        obj.Food_id=vfid
        obj.Customer_name=vcus
        obj.Product_name=vpname
        obj.Product_quntity=vpquntity
        obj.Product_prize=vprize
        obj.address=vadd
        obj.Date_time=vdt
        obj.save()
        return redirect('/viewfood')
    
# def insertregister(request):
#       if request.method=='POST':
#          vfname=request.POST.get('fname')
#          vlname=request.POST.get('lname')
#          vuname=request.POST.get('uname')
#          vpass=request.POST.get('pass')
#          obj=ViewRegister()
#          obj.First_name=vfname
#          obj.Last_name=vlname
#          obj.user_name=vuname
#          obj.password=vpass
#          obj.save()
#          return redirect('/')

def insertregister(request):
    if request.method=='POST':
        vfname=request.POST.get('fname')
        vlname=request.POST.get('lname')
        vuname=request.POST.get('uname')
        vpass=request.POST.get('pass')
        cpass=request.POST.get('cpass')
        if vpass==cpass:
             if User.objects.filter(username=vuname).exists():
                messages.success(request,'The username is already registered')
                return redirect('/register')
             else:
                 newuser=User.objects.create_user(first_name=vfname,last_name=vlname,username=vuname,password=vpass)
                 newuser.save()
                 messages.success(request,'User registration is done')
                 return redirect('/')
        else:
             return redirect('/register')
        

    
def displayregister(request):
    regobj=ViewRegister.objects.all()
    return render(request,'viewregister.html',{'data':regobj})

def delreg(request,fid):
    reg=ViewRegister.objects.get(id=fid)
    reg.delete()
    return redirect('/viewreg')

def delfeed(request,fid):
    feed=userfeedback.objects.get(id=fid)
    feed.delete()
    return redirect('/display')

def aboutuspage(request):
    return render(request,'aboutus.html')

def userlogin(request):
    return render(request,'userlogin.html')

def authlogin(request):
    if request.method=='POST':
        vuname=request.POST.get('uname')
        vpass=request.POST.get('upass')
        user=auth.authenticate(username=vuname,password=vpass)
        if user is not None:
            auth.login(request,user)
            return redirect('/userpage')
        else:
            return redirect('/userlog')

def Userloadpage(request):
     if request.user.is_authenticated:
        return render(request,'userpage.html')
     else:
         return redirect('/userlog')

def addfoodcart(request):
    addcart=AddtoCart.objects.all()
    return render(request,'addfoodcart.html',{'cart':addcart})

def logOut(request):
    auth.logout(request)
    messages.success(request,'sucessfully logged out')
    return redirect('/')

def contactus(request):
    return render(request,'Contactus.html')

def vieworderfood(request):
    orderfood=AddtoCart.objects.all()
    return render(request,'viewaddtocart.html',{'cart':orderfood})

def buyproductpage(request):
    return render(request,'buyproduct.html')

def delorderfood(request,fid):
    feed=Buyproduct.objects.get(id=fid)
    feed.delete()
    return redirect('viewbuy')

def viewbuyfood(request):
    buyfood=Buyproduct.objects.all()
    return render(request,'viewbuyproduct.html',{'cart':buyfood})

def insertbuyfood(request):
    if request.method=='POST':
        vpname=request.POST.get('pname')
        vquntity=request.POST.get('proq')
        vcadd=request.POST.get('cadd')
        obj=Buyproduct()
        obj.cus_pro=vpname
        obj.quntity=vquntity
        obj.cus_add=vcadd
        obj.save()
        return redirect('viewbuy')