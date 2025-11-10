from django.urls import path
from App1.views import Showform,Form,Formdelete,Formedit,Formupdate

urlpatterns = [
    path('',Form,name='form'),
    path('showform',Showform,name='showform'),
    path('update/<int:Task_id>/',Formupdate,name='formupdate'),
    path('delete/<int:Task_id>/',Formdelete,name='formdelete'),
    path('edit/<int:Task_id>/',Formedit,name='formedit')
]
