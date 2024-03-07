from django.contrib import admin
from .models import Patient,Doctor,Appoinment,department,Login

# Register your models here.

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appoinment)
admin.site.register(department)
admin.site.register(Login)

