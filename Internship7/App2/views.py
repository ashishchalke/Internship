from django.shortcuts import render,redirect
from . models import Leave_Quota
from . forms import Leave_Quotaform

# Create your views here.
def Leave_quota(request):
    if request.method =='POST':
        data = Leave_Quotaform(request.POST)
        if data.is_valid():
            data.save()
            return redirect('leave_quotashow')
    else:
        data = Leave_Quotaform()
    return render(request,'App2/leave_quota.html',{'form':data})

def Leave_quotaShow(request):
    data = Leave_Quota.objects.all()
    return render (request,'App2/leave_quotaShow.html',{'range1':data})

def Leave_quotaEdit(request,quotaid):
    data = Leave_Quota.objects.get(quotaid=quotaid)
    return render(request,'App2/leave_quotaedit.html',{'range1':data})

def Leave_quotaUpdate(request,quotaid):
    obj = Leave_Quota.objects.get(quotaid=quotaid)
    data = Leave_Quotaform(request.POST,instance=obj)
    
    if data.is_valid():
        data.save()
        return redirect('leave_quotashow')
    
def Leave_quotaDelete(request,quotaid):
    data = Leave_Quota.objects.get(quotaid=quotaid)
    data.delete()
    return redirect('leave_quotashow')