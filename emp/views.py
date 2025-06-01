from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import emp
# Create your views here.
def emp_home(request):
    emps=emp.objects. all()
    
    return render(request,"emp/home.html",{})

def add_emp(request):
    if request.method=="POST":
       #data fetch
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")
       #cerate model object
        e=emp()
        e.emp_name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        e.save()   
        

        
       #cerate model object 
       
       #save the object

       #prepare mrg

        return redirect("/emp/home")
    return render(request,"emp/add_emp.html",{})