from django.urls import path
from App.views import review,showreview,employee,editreview,updatereview,deletereview

urlpatterns = [
    path('review',review,name='review'),
    path('showreview',showreview,name='showreview'),
    path('',employee,name='employee'),
    path('edit/<int:Review_Id>/',editreview,name='editreview'),
    path('update/<int:Review_Id>/',updatereview,name='updatereview'),
    path('delete/<int:Review_Id>/',deletereview,name='deletereview')
]
