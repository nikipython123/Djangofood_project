from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('feed',views.feedback,name='feed'),
    path('display',views.displayfeed,name='display'),
    path('insertfeed',views.insertfeedback),
    path('adminlog',views.adminlogin),
    path('adminpage',views.adminpage,name='adminpage'),
    path('register',views.registerlogin,name='register'),
    path('food',views.foodpage,name='food'),
    path('addfood',views.insertfood),
    path('viewfood',views.displayfood,name='viewfood'),
    path('delete<int:fid>',views.delFood,name='delete'),
    path('edit/<int:fid>',views.editfood,name='edit'),
    path('update/<int:fid>',views.updatefood,name='updatepage'),
    path('insertreg',views.insertregister),
    path('viewreg',views.displayregister,name='viewreg'),
    path('del<int:fid>',views.delreg,name='del'),
    path('delfeedback<int:fid>',views.delfeed,name='delfeedback'),
    path('about',views.aboutuspage,name='about'),
    path('userlog',views.userlogin,name='userlog'),
    path('authuser',views.authlogin),
    path('userpage',views.Userpage,name='userpage'),
    path('foodcart',views.addfoodcart,name='foodcart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)