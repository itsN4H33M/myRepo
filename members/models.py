from django.db import models

DEPARTMENT_CHOICES = (
    ("SALES", "SALES"),
    ("MARKETING", "MARKETNIG"),
    ("HR", "HR"),
    ("FINANCE", "FINANCE"),
)

# Create your models here.
class Employees(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    employee_id = models.IntegerField()
    mobile = models.CharField(max_length=10)
    dept = models.CharField(max_length=10, choices=DEPARTMENT_CHOICES)

    def __str__(self):
        return self.first_name + " " + self.last_name
