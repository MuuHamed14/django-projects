from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'index1.html',{})
def p(request):
    return render(request,'index1.html',{})
def page1(request):
    return render(request,'python.html',{})
def page2(request):
    return render(request,'java.html',{})
def page3(request):
    return render(request,'Android.html',{})
def p1(request):
    con = {'first_name':'Hamaza','last_name':'MuuHamed','age':14,'list':[1,2,3]}
    return render(request,'index.html',con)
def p2(request):
    return HttpResponse('django and python 3 ')
def p3(request):
    s = '''
     <html>
        <head>
            <title> pro 2 </title>
        </head>
     <body>
        <h1> its good for using django </h1>
     </body>
     </html>
    '''
    return HttpResponse(s)
def p4(request,n1,n2):
    s = n1 + n2
    return HttpResponse('The sum is :' + str(s))
def p5(request,a,b):
    return HttpResponse(a + ' ' + str(b))
def p6(request,a,b,c):
    return HttpResponse(a + ' ' + str(b + c))