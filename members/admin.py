from django.contrib import admin
from .models import Employees

class DjEmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "address", "employee_id", "mobile", "dept")
    list_filter = ("dept",)

# Register your models here.
admin.site.register(Employees, DjEmployeeAdmin) 
