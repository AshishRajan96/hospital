from  django import forms
from.models import Patient,Doctor,Appoinment,department,Login

class patientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"
        widgets = {

         }
        
class doctorform(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"
        widgets = {

         }

class appoinmentForm(forms.ModelForm):
    class Meta:
        model = Appoinment
        fields = "__all__"
        widgets={

        }

class departmentForm(forms.ModelForm):
    class meta:
        model = department
        feilds = "__all__"
        widgets= {

        }

class loginform(forms.ModelForm):
    class meta:
        model = Login
        feils = "__all__"
        widgets= {

        }