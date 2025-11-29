from django.db import models

# Create your models here.
class Login(models.Model):
    uname=models.CharField(max_length=10, primary_key=True)
    passw=models.CharField(max_length=10)

    class Meta:
        db_table='login'




class Collage(models.Model):
    cname=models.CharField(max_length=100)
    city=models.CharField(max_length=52)
    crs=models.CharField(max_length=20)
    em=models.CharField(max_length=40)
    cno=models.CharField(max_length=12)
    addr=models.CharField(max_length=80)
    loc=models.CharField(max_length=50)
    img=models.ImageField(upload_to='')
    id=models.AutoField(primary_key=True)

    class Meta:
        db_table='collage'


class Enquiry(models.Model):
    cid=models.CharField(max_length=30)
    name=models.CharField(max_length=52)
    cno=models.CharField(max_length=12)
    city=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    qry=models.CharField(max_length=200)
    id=models.AutoField(primary_key=True)

    class Meta:
        db_table='enquiry'


class Callme(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=52)
    phone=models.CharField(max_length=12)
    query=models.CharField(max_length=200)

    class Meta:
        db_table='callme'

class Forgotps(models.Model):
    newpass=models.CharField(max_length=30)
    conformpass=models.CharField(max_length=52)
    
    class Meta:
        db_table='forgot'



