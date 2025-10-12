from django.urls import path
from App1.views import formsview,formshow,editform,updateform,deleteform

urlpatterns = [
    path('',formsview,name='formview'),
    path('formshow',formshow,name='formshow'),
    path('edit/<int:SrNo>/',editform,name='editform'),
    path('update/<int:SrNo>/',updateform,name='updateform'),
    path('delete/<int:SrNo>/',deleteform,name='deleteform')
]
