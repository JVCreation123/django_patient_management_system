from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Bookdata1)
admin.site.register(Paymentdata1)

admin.site.register(Pateintlogin1)
admin.site.register(Announcement_md1)
admin.site.register(Patientdata1)
admin.site.register(Prescriptiondata1)


class Bookdata1(admin.ModelAdmin):
    list_display = ('name','gender','dob','visit','adate','atime')

class Prescriptiondata1(admin.ModelAdmin):
    list_display1 = ('Name','Medicine','Date')