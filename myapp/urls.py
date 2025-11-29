from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
  
     path('', views.home, name='home page'),
     path('contact', views.contact, name='contact page'),
     path('login', views.login, name='login page'),
     path('logout', views.logout, name='login page'),
     path('register', views.register, name='register page'),
     path('checkuser', views.checkuser, name='other page'),
     path('resetpass', views.resetpass, name='resetpass page'),
     path('changepass', views.changepass, name='changepass page'),
     path('addcollage', views.addcollage, name='addcollage page'),
     path('account', views.account, name='account page'),
     path('savecollage', views.savecollage, name='savecollage page'),
     path('record', views.viewrecord, name='record page'),
     path('delcollage/<id>', views.delcollage, name='delete data '),
     path('editcollage/<id>', views.editcollage, name='edit data '),
     path('updatecollage', views.updatecollage, name='update data '),
     path('selectby', views.selectby, name='selectby data '),
     path('enquiryhere/<id>', views.enquiryhere, name='enquiry here data '),
     path('saveenquiry', views.saveenquiry, name='saveenquiry data'),
     path('viewenquiry/<cid>', views.viewenquiry, name='edit data '),
     path('delenquiry/<id>', views.delenquiry, name='delete enquiry data '),
     path('contactdata', views.contactdata, name='contact data '),
     path('forgotpass', views.forgotpass, name='forgot password data '),
     path('forgotpassword', views.forgotpassword, name='forgot password data '),
     path('click', views.click, name='click to go home page '),
     path('clickto', views.clickto, name='click to go home page '),
     path('getappoint', views.getappoint, name='click to go contact page '),
     path('get', views.get, name='click to go contact page '),

]
