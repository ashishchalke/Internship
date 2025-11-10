from django.shortcuts import render,redirect
from . models import Taskmodel
from . forms import Taskform

# Create your views here.
def Form(request):
    if request.method == 'POST':
        data = Taskform(request.POST)
        
        if data.is_valid():
            data.save()
            return redirect('showform')
    else:
        data = Taskform()
    return render(request,'App1/Forms.html',{'form':data})
        

def Showform(request):
    data = Taskmodel.objects.all()
    return render(request,'App1/Showform.html',{'range':data})


def Formedit(request,Task_id):
    data = Taskmodel.objects.get(Task_id=Task_id)
    return render(request,'App1/Formedit.html',{'range':data})

def Formupdate(request,Task_id):
    obj = Taskmodel.objects.get(Task_id=Task_id)
    data = Taskform(request.POST,instance=obj)
    
    if data.is_valid():
        data.save()
        return redirect('showform')

def Formdelete(request,Task_id):
    data = Taskmodel.objects.get(Task_id=Task_id)
    data.delete()
    return redirect('showform')