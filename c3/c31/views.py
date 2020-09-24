from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from c31.forms import staff_form , pic_form
from c31.models import staff , info , pic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
def index(request):
    return HttpResponse(' Welcome To project 3 ')
#forms
def reg(request):
    form = staff_form(request.POST or None)
    obj = staff()
    if form.is_valid():
        if not request.POST['birthday']:
            obj.birthday = '1997-01-8'
        else:
            obj.birthday = form.cleaned_data['birthday']
        if not request.POST['email']:
            obj.email = 'default@yahoo.com'
        else:
            obj.email = form.cleaned_data['email']
        obj.fullname = form.cleaned_data['fullname']
        # obj.email = form.cleaned_data['email']
        obj.age = form.cleaned_data['age']
        # obj.birthday = form.cleaned_data['birthday']
        print('The name is :' + form.cleaned_data['fullname'])
        obj.save()
        return HttpResponseRedirect('/c3/')
    return render(request,'staff_reg.html',{'f':form})
#register
def register(request):
    return render(request,'register.html',{})
def register_backend(request):
    try:
        user = User.objects.create_user(request.POST['username'], request.POST['email'],request.POST['password'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        return HttpResponseRedirect('/c3/')
    except :
        return HttpResponse('user is exists')
#profile
def profile(request,username):
    return render(request,'profile.html',{'u':username})
#login
def log(request):
    return render(request,'login.html',{})
def log_backend(request):
    u = request.POST['username']
    p = request.POST['password']
    re = authenticate(username = u , password = p)
    if re is not None :
        print('login')
        login(request,re)
        link = '/c3/profile/'+ str(re)
        return HttpResponseRedirect(link)
    else:
        return HttpResponse('user is not exist')
#logout
def logout_backend(request):
    logout(request)
    return HttpResponse(' you logout now ')

#log_info
def log_info(request,username):
    return render(request,'log_info.html',{'username':username})
def loginfo_backend(request,username):
    u = info()
    user = User.objects.get(username = username )
    u.jobs = request.POST['jobs']
    u.lang = request.POST['lang']
    u.number = request.POST['num']
    u.username = user
    u.save()
    return HttpResponse('Yes I Do')
#show data
def show_user(request,username):
    user = User.objects.get(username = username)
    inf = info.objects.filter(username = user)
    con = {'u1':user,'u2':inf}
    return render(request,'how_data.html',con)

#upload image

def upload_image(request):
    u = pic()
    form = pic_form(request.POST,request.FILES)
    if form.is_valid():
        u.name = request.POST['name']
        u.img = form.cleaned_data['img']
        u.save()
        return HttpResponse('yes I do')
    return render(request,'image.html',{'f':form})
