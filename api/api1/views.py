from django.shortcuts import render
from django.http import HttpResponse
from .json import jsonstudent ,  json_user
from .models import student
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import viewsets
import requests

def index(request):
    return HttpResponse(' Welcome to Rest Api ')

# first way
class student_list(APIView):

      def get(self,request):

          s1 = student.objects.all()
          s2 = jsonstudent(s1,many = True)
          return Response(s2.data) # return data
      def post(self):
         pass

#other way

class student_list1(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = jsonstudent

class userjson(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = json_user

#requests
def get_data(request):
    url = 'http://rawan.pythonanywhere.com/studentjson1/'
    data = requests.get(url).json()
    print(data)
    return render(request,'in.html',{'d':data})