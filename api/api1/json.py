from rest_framework import serializers
from .models import student
from django.contrib.auth.models import User
class jsonstudent(serializers.ModelSerializer):
    class Meta :
        model = student
        fields = '__all__' # fields = ['id','name'] if you want to select fields

class json_user(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = '__all__'