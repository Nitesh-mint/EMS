from django.shortcuts import render
from .models import Employee
from django.views.generic import ListView

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees.html'