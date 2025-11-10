from django.urls import path
from App1.views import Leaveview,Managerview,Employeeview,LeaveShow,Leavedelete,Leaveedit,Leaveupdate


urlpatterns = [
    path('leave',Leaveview,name='leave'),
    path('',Managerview,name='manager'),
    path('employee',Employeeview,name='employee'),
    path('leaveshow',LeaveShow,name='leaveshow'),
    path('update/<int:leaveid>/',Leaveupdate,name='leaveupdate'),
    path('delete/<int:leaveid>/',Leavedelete,name='leavedelete'),
    path('edit/<int:leaveid>/',Leaveedit,name='leaveedit')
]
