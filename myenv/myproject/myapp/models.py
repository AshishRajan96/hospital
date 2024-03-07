from django.db import models

# Create your models here.

class Patient(models.Model):
    patientname=models.CharField(max_length=200)
    age=models.CharField(max_length=200,null=True)
    Email=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=200)
    gender=models.CharField(max_length=200,null=True)

    contact=models.CharField(max_length=200)
    username=models.CharField(max_length=150)
    password=models.CharField(max_length=200)
    password1=models.CharField(max_length=200)
    def _str_(self):
        return self.patientname



class Doctor(models.Model):
    doctorname=models.CharField(max_length=200)
    speciality=models.CharField(max_length=250)
    age=models.CharField(max_length=200,null=True)
    Email=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=200)
    gender=models.CharField(max_length=200,null=True)
    contact=models.CharField(max_length=200)
    qualification=models.CharField(max_length=200)
    days=models.CharField(max_length=250)
    time=models.CharField(max_length=200)
    username=models.CharField(max_length=150)
    password=models.CharField(max_length=200)
    password1=models.CharField(max_length=200)
    def _str_(self):
        return self.doctorname
    
class Login(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    def _str_(self):
        return self.username

class Appoinment(models.Model):
    name=models.CharField(max_length=200)
    datepicker=models.CharField(max_length=200,null=True)
    symptoms=models.CharField(max_length=200)
    def str(self):
        return self.name

class department(models.Model):
    departmentnumber = models.CharField(max_length=200)
    departmentname = models.CharField(max_length=200,null=True)
    doctorname = models.CharField(max_length=200, null=True)

    def str(self):
        return self.departmentname

class Login(models.Model):
    username = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200,null=True)

    def str(self):
        return self.username


    



