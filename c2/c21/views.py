from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .models import company

#show data
def index(request):
    data = company.objects.all()
    return render(request,'show_data.html',{'d':data})
#end

#inserted data
def create_company(request):
    return render(request,'form_create.html',{})
def backend1(request):
    v1 = request.POST['fullname']
    v2 = request.POST['email']
    v3 = request.POST['age']
    v4 = request.POST['birthday']
    new = company(fullname = v1 , email = v2 , age = v3 , birthday = v4)
    new.save()
    return HttpResponseRedirect('/c21')
#end inserted

#updated data
def update_company(request,id):
     # all()

     data = company.objects.all()
     # data = company.objects.all()[0:5]
     # print('The Type is :' + str(data)) #  All obj return
     # print('The Type is : ' + str(data[0])) # first obj
     # print('The Type is : ' + str(data[0].fullname)) # fullname is return
     return render(request,'form_update.html',{'id':id,'d':data[id-1]})

    #filter()

    # data = company.objects.filter(id = id )
    # data = company.objects.filter(id__in = [1,2,5])
    # data = company.objects.filter(age__in=[16,22])
    # data = company.objects.filter(fullname__in=['Aya'])
    # data = company.objects.filter(id =1 , fullname ='Hamaza') # return obj 1
    # data = company.objects.filter(id = 1 , fullname = 'aya') # return empty obj
    # data = company.objects.filter(age__gte = 12) # age > 12
    # data = company.objects.filter(age__lte = 21)  # age < 12
    # data = company.objects.order_by('age') # retuen data order by age
    # print('the type is ' + str(data))
    # return render(request, 'form_update.html', {'id': id, 'd': data})

    # get()

    # data = company.objects.get(fullname = 'Aya') # return obj with fullname Aya
    # data = company.objects.get(id = id) # return obj one only
    # print('The Type is : ' + str(data))
    # return render(request, 'form_update.html', {'id': id, 'd': data})

def backend2(request,id):
    v1 = request.POST['fullname']
    v2 = request.POST['email']
    v3 = request.POST['age']
    v4 = request.POST['birthday']
    old = company( id = id ,fullname = v1 , email = v2 , age = v3 , birthday = v4)
    old.save()
    return HttpResponseRedirect('/c21')
#end updated

#deleted data
def backend3(request,id):
    old = company(id = id)
    old.delete()
    return HttpResponseRedirect('/c21')
#end deleted data