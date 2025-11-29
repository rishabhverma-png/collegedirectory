from django.shortcuts import render,HttpResponse,redirect
from myapp.models import Login,Collage,Enquiry,Callme


# Create your views here.
def home(request):
   data=Collage.objects.all()
   return render(request,'home.html',{'data':data})
def contact(request):
    return render(request,'contact.html')
def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')
def checkuser(request):
    un=request.POST["uname"];
    ps=request.POST["passw"];
    found=Login.objects.filter(uname=un,passw=ps).exists()
    if found==True:
        request.session['un']=un;
        request.session['ps']=ps;
        return render(request,'cpanel/adminhome.html')
    else:
        return HttpResponse('please enter correct username and password')
    
def logout(request):
    return render(request,'cpanel/logout.html')

def resetpass(request):
    return render(request,'cpanel/resetpass.html')

def changepass(request):
    nps=request.POST["nps"];
    cps=request.POST["cps"];
    
    if nps==cps :
        un=request.session['un'];
        Login.objects.filter(uname=un).update(passw=nps)
        return render(request,'cpanel/adminhome.html')
    else:
        return HttpResponse('does not match nps and cps ')
    

def addcollage(request):
    return render(request,'cpanel/addcollage.html')
def account(request):
    return render(request,'cpanel/addcollage.html')
def savecollage(request):
    cname1=request.POST["cname"];
    city1=request.POST["city"];
    crs1=request.POST["crs"];
    em1=request.POST["em"];
    cno1=request.POST["cno"];
    addr1=request.POST["addr"];
    loc1=request.POST["loc"];
    img1=request.FILES["img"];
    Collage(city=city1,cname=cname1,crs=crs1,em=em1,cno=cno1,addr=addr1,loc=loc1,img=img1).save()
    return HttpResponse('SUBMITTED SUCCESFULLY')
def record(request):
    return render(request,'cpanel/viewrecord.html')
def viewrecord(request):
    data=Collage.objects.all()
    return render(request,'cpanel/viewrecord.html',{'data':data})

def delcollage(request,id):
    Collage.objects.filter(id=id).delete()
    return redirect('/record')

def editcollage(request,id):
    data=Collage.objects.filter(id=id)
    return render(request,'cpanel/editcollage.html',{'data':data})

def updatecollage(request):
    id1=request.POST["id"];
    cname1=request.POST["cname"];
    city1=request.POST["city"];
    crs1=request.POST["crs"];
    em1=request.POST["em"];
    cno1=request.POST["cno"];
    addr1=request.POST["addr"];
    loc1=request.POST["loc"];
    
    Collage.objects.filter(id=id1).update(city=city1,cname=cname1,crs=crs1,em=em1,cno=cno1,addr=addr1,loc=loc1)
    return HttpResponse('UPDATE SUCCESFULLY')


def selectby(request):
    city1=request.POST["city"];
    if city1!="Null":
      data=Collage.objects.filter(city=city1).all()
    else: 
      data=Collage.objects.all() 
    return render(request,'home.html',{'data':data})

def enquiryhere(request,id):
    return render(request,'enquiry.html',{'id':id})


def saveenquiry(request):
    cid1=request.POST["cid"];
    name1=request.POST["name"];
    cno1=request.POST["cno"];
    city1=request.POST["city"];
    email1=request.POST["email"];
    qry1=request.POST["qry"];
    Enquiry(cid=cid1,name=name1,cno=cno1,city=city1,email=email1,qry=qry1).save()
    return HttpResponse('SUBMITTED SUCCESFULLY')

def viewenquiry(request,cid):
    data=Enquiry.objects.filter(cid=cid)
    return render(request,'cpanel/viewenquiry.html',{'data':data})

def delenquiry(request,id):
    Enquiry.objects.filter(id=id).delete()
    return redirect('/viewenquiry/'+id)

def contactdata(request):
    name1=request.POST["name"];
    email1=request.POST["email"];
    phone1=request.POST["phone"];
    query1=request.POST["query"];
    Callme(name=name1,email=email1,phone=phone1,query=query1).save()
    return HttpResponse('SUBMITTED SUCCESFULLY')

def forgotpass(request):
    return render(request,'forgotpass.html')

def forgotpassword(request):
    newpass=request.POST["newpass"];
    conformpass=request.POST["conformpass"];
    
    if newpass==conformpass :
        un=request.session['un'];
        Login.objects.filter(uname=un).update(passw=newpass)
        return render(request,'login.html')
    else:
        return HttpResponse('does not match nps and cps ')
    
def click(request):
    return render(request,'home.html')
def clickto(request):
    return render(request,'home.html')

def getappoint(request):
    return render(request,'contact.html')
def get(request):
    return render(request,'contact.html')









