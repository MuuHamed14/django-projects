from django.urls import path , include
from api1.views import index , student_list , student_list1 , userjson , get_data
from rest_framework import routers
r = routers.DefaultRouter()
r.register('',student_list1)
r1 = routers.DefaultRouter()
r1.register('show/',userjson)

urlpatterns = [
    path('',index,name ='index'),
    path('studentjson/',student_list.as_view()),
    path('studentjson1/',include(r.urls)),
    path('user/',include(r1.urls)),
    path('doc/',get_data,name ='get_data'),
]