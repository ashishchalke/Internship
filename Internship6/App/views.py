from django.shortcuts import render,redirect
from . models import Review,Employee
from . forms import Reviewform,Employeeform


# Create your views here.
def review(request):
    if request.method == 'POST':
        data = Reviewform(request.POST)
        
        if data.is_valid():
            data.save()
            return redirect('showreview')
        
    else:
        data = Reviewform()
    return render(request,'App/Review.html',{'form':data})

def employee(request):
    if request.method == 'POST':
        data = Employeeform(request.POST)
        
        if data.is_valid():
            data.save()
            return redirect('review')
        
    else:
        data = Employeeform()
    return render(request,'App/Employee.html',{'form':data})


def showreview(request):
    data = Review.objects.all()
    return render(request,'App/ShowReview.html',{'range':data})

def editreview(request,Review_Id):
    data = Review.objects.get(Review_Id=Review_Id)
    return render(request,'App/ReviewEdit.html',{'range':data})

def updatereview(request,Review_Id):
    obj = Review.objects.get(Review_Id=Review_Id)
    data = Reviewform(request.POST,instance=obj)
    
    if data.is_valid():
        data.save()
        return redirect('showreview')
    
def deletereview(request,Review_Id):
    data = Review.objects.get(Review_Id=Review_Id)
    
    data.delete()
    return redirect('showreview')