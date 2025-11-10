from django.urls import path
from App2.views import Leave_quota,Leave_quotaShow,Leave_quotaDelete,Leave_quotaEdit,Leave_quotaUpdate


urlpatterns = [
    path('',Leave_quota,name='leave_quota'),
    path('leave_quotashow',Leave_quotaShow,name='leave_quotashow'),
    path('delete/<int:quotaid>/',Leave_quotaUpdate,name='leave_quotaupdate'),
    path('update/<int:quotaid>/',Leave_quotaEdit,name='leave_quotaedit'),
    path('edit/<int:quotaid>/',Leave_quotaDelete,name='leave_quotadelete')
    
]



