"""firstsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cs.views import p,p1 , p2 , p3 , p4 , p5 , p6 , page1 , page2 , page3 , home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home , name ='home'),
    path('',p,name = 'index'),
    path('python/',page1,name='python'),
    path('java/',page2,name = 'java'),
    path('android/',page3,name ='android'),
    path('p5/',p1 , name = 'index'),
    path('p/',p2 , name = 'p'),
    path('p1/',p3 , name = 'p1'),
    path('p2/<int:n1>/<int:n2>/',p4 , name = 'p2'),
    path('p3/<str:a>/<int:b>/',p5,name = 'p3'),
    path('p4/<str:a>/<int:b>/<int:c>/',p6,name = 'p4'),
]
