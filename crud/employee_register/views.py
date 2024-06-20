from django.shortcuts import render, redirect

from .models import Employee
from .forms import EmployeeForm

def employee_list(request):
    employees = Employee.objects.all()

    context = {
        'employees' : employees
    }

    return render(request, 'employee_register/employee_list.html', context)


def employee_form(request, id=0):

    if request.method == 'GET':
        if id == 0: # empty form
            form = EmployeeForm()
        else: # form with data
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        context = {'form':form}
        return render(request, 'employee_register/employee_form.html', context)
    
    if request.method == 'POST':
        if id == 0: # new Employee
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_register:employee_list')


def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('employee_register:employee_list')
