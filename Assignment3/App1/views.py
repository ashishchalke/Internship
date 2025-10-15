from django.shortcuts import render,redirect
from . models import Employee
from .forms import Empform

# Create your views here.
def Emp(request):
    if request.method == 'POST':
        data = Empform(request.POST)
        
        if data.is_valid():
            data.save()
            return redirect('empshow')
    else:
        data = Empform()
    return render(request,'App1/Empform.html',{'form':data})

def Empshow(request):
    data = Employee.objects.all()
    return render(request,'App1/Emptable.html',{'range':data})

def Empedit(requst,SrNo):
    data = Employee.objects.get(SrNo = SrNo)
    return render(requst,'App1/Empedit.html',{'range':data})

def Empupdate(request,SrNo):
    obj = Employee.objects.get(SrNo = SrNo)
    data = Empform(request.POST,instance=obj)
    
    if data.is_valid():
        data.save()
        return redirect('empshow')
    
def Empdelete(request,SrNo):
    data = Employee.objects.get(SrNo = SrNo)
    data.delete()
    return redirect('empshow')