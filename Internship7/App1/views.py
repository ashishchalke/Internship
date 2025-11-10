from django.shortcuts import render,redirect
from .models import Employeemodel,Leavemodel,Managermodel
from . forms import Employeeform,Leaveform,Managerform
# Create your views here.
def Leaveview(request):
    if request.method == "POST":
        data = Leaveform(request.POST)
        
        if data.is_valid():
            data.save()
            return redirect('leaveshow')
        
    else:
        data = Leaveform()
    return render(request,'App1/Leave.html',{'form':data})

def Leaveedit(request,leaveid):
    data = Leavemodel.objects.get(leaveid=leaveid)
    return render(request,'App1/LeaveEdit.html',{'range':data})

def Leaveupdate(request,leaveid):
    obj = Leavemodel.objects.get(leaveid=leaveid)
    data = Leaveform(request.POST,instance=obj)
    if data.is_valid():
        data.save()
        return redirect('leaveshow')
    
def Leavedelete(request,leaveid):
    data = Leavemodel.objects.get(leaveid=leaveid)
    data.delete()
    return redirect('leaveshow')

def LeaveShow(request):
    data = Leavemodel.objects.all()
    return render(request,'App1/Leavetable.html',{'range':data})


def Employeeview(request):
    if request.method == "POST":
        data = Employeeform(request.POST)
        
        if data.is_valid():
            data.save()
            return redirect('leave')
        
    else:
        data = Employeeform()
    return render(request,'App1/Employee.html',{'form':data})

def Managerview(request):
    if request.method == "POST":
        data = Managerform(request.POST)
        
        if data.is_valid():
            data.save()
            return redirect('employee')
        
    else:
        data = Managerform()
    return render(request,'App1/Manager.html',{'form':data})


