from django.urls import path
from App1.views import Emp,Empshow,Empedit,Empupdate,Empdelete

urlpatterns = [
    path('',Emp,name='emp'),
    path('empshow',Empshow,name='empshow'),
    path('empedit/<int:SrNo>/',Empedit,name='empedit'),
    path('empupdate/<int:SrNo>/',Empupdate,name='empupdate'),
    path('empdelete/<int:SrNo>/',Empdelete,name='empdelete')
]
