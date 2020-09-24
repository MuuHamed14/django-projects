from django.urls import path
from c31.views import index , reg , register , register_backend , log , log_backend , profile , logout_backend , log_info ,loginfo_backend , show_user ,  upload_image
urlpatterns = [
    path('', index , name = 'index'),
    path('reg/',reg,name ='reg'),
    path('register/',register,name ='register'),
    path('register_backend/',register_backend,name ='register_backend'),
    path('log/',log,name = 'log'),
    path('log_backend/',log_backend ,name = 'log_backend'),
    path('profile/<str:username>/',profile,name = 'profile'),
    path('logout_backend/',logout_backend,name = 'logout_backend'),
    path('log_info/<str:username>/',log_info,name = 'log_info'),
    path('loginfo_backend/<str:username>/',loginfo_backend,name = 'loginfo_backend'),
    path('show_user/<str:username>/',show_user,name ='show_user'),
    path('pic/', upload_image,name ='pic'),
]
