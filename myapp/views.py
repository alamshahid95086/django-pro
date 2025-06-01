from django.http import HttpResponse
import datetime
from django.shortcuts import  render




def web(request):
   isActive=True
   if request.method=='POST':
     check=request.POST.get("check")
     print(check)
     if check is None: isActive=False
     else:
        isActive=True

   date=datetime.datetime.now()
  
   name="SHAHID"
   list_of_program=[
       'WAP to check even or odd',
       'WAP to check prime number',
       'WAP to print all prime number from 1 to 100'  
                   ]
   student={ 
       'student_name' :"shahid",
       'student_college':"RLSYC",
       'student_city':"aurangabad"


   }
   data={
       'date':date,
       'isActive':isActive,
       'name':name,
       'list_of_program':list_of_program,
       'student_data':student

   }


   return render (request,"web.html",data)
 

def home (request):
    
    print("test function is called from views ")
    return render(request,"home.html",{ })
def Company(request):
    return render(request,"company_details.html",{ })

def services (request):
    # return HttpResponse("this is services page")
    return render (request ,"services.html",{ })

