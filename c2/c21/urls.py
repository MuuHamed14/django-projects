from django.urls import path
from c21.views import index , create_company , backend1 , update_company , backend2 , backend3

urlpatterns = [
    path('',index,name ='index'),
    path('create_company/',create_company,name = 'create_company'),
    path('backend1/',backend1,name = 'backend1'),
    path('update_company/<int:id>/',update_company,name = 'update_company'),
    path('backend2/<int:id>/',backend2,name = 'backend2'),
    path('backend3/<int:id>/', backend3, name='backend3'),
]
