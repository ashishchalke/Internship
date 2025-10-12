from django.shortcuts import render,redirect
from .models import Formsmodel
from .forms import Formsform

# Create your views here.
def formsview(request):
    if request.method == 'POST':
        data = Formsform(request.POST)
        if data.is_valid():
            data.save()
            return redirect('formshow')
    else:
        data = Formsform()
    return render(request,'App1/Form.html',{'form':data})

def formshow(request):
    data = Formsmodel.objects.all()
    return render(request,'App1/Showform.html',{'range':data})

def editform(request,SrNo):
    data = Formsmodel.objects.get(SrNo=SrNo)
    return render(request,'App1/Editform.html',{'range':data})

def updateform(request,SrNo):
    form = Formsmodel.objects.get(SrNo=SrNo)
    data = Formsform(request.POST,instance=form)
    
    if data.is_valid():
        data.save()
        return redirect('formshow')

def deleteform(request,SrNo):
    data = Formsmodel.objects.get(SrNo=SrNo)
    data.delete()
    return redirect('formshow')
        