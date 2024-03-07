from django.shortcuts import render,redirect
from.forms import patientForm,doctorform,appoinmentForm
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from.models import Patient,Doctor,Appoinment,Login




# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def departments(request):
    return render(request,'departments.html')
def doctors(request):
    return render(request,'doctors.html')
def contact(request):
    return render(request,'contact.html')
def readmore(request):
    return render(request,'readmore.html')



def registration(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        password1=request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():

                messages.info=(request,"user taken")
                return redirect("registration")
                user=User.objects.create_user(username=username,password=password)
                user.save()
        else:
            return render('registration')
        return render(request,'index.html')
    else:
        return render(request,'registration.html')




def doctorregistration(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                # messages.info(request,"username taken")
                return redirect('doctorregistration')
                user = User.objects.create_user(username=username, password=password)
                user.save()
                print("user created")
        else:
            print("password not matched")
            return redirect('doctorregistration')
        return render(request, 'index.html')
    else:
        return render(request, 'doctorregistration.html')

def appoinment(request):
    return render(request, 'appoinment.html')

    '''if request.method == "POST":
        form=appoinmentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
        else:
            form = appoinmentForm()'''


def deptreg(request):
    return render(request, 'deptreg.html')


def adminmodule(request):
    return render(request, 'adminmodule.html')
def usermodule(request):
    return render(request, 'usermodule.html')
def drmodule(request):
    return render(request, 'drmodule.html')
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user=Patient.objects.get(username=username,password=password)
            if user is not None:
                print(user)
                return render(request,'usermodule.html')
            return render(request, 'login.html')
        except:
             pass
        try:
           user=Login.objects.get(username=username,password=password)
           if user is not None:
               print(user)
               return render(request, 'index.html')
           #return render(request,'Adminmodule.html')
        except:
            pass

        try:
            user=Doctor.objects.get(username=username,password=password)
            if user is not None:
                print(user)
                return render(request,'drmodule.html')
            return render(request,'login.html')
        except:
             pass
    else:
        return render(request,'login.html')

def viewpatient(request):
    return render(request,'viewpatient.html')
def adminapprove(request):
    return HttpResponse("<h2>Your Appoinment is Approved</h2>")
def LoginFrm(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form['username'].valid()
            password=form['password'].valid()
            try:
                user=Login.objects.get(username=username,password=password)
                if user is not None:
                    return render(request,'index.html')
            except:
               pass
    else:
        return render(request, 'LoginFrm.html')


