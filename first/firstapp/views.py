from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexfun(request):
    peoples = [
        {'name':'sandeep', 'sharp':65},
        {'name':'yakshit', 'sharp':75}, 
        {'name':'vamsi', 'sharp':71}, 
    ]

    return render(request,'first/index.html',{'peoples':peoples,'page':'index'})

def basefun(request):
    context = {'page':'base'}
    return render(request,'base.html',context)

def aboutfun(request):
    context = {'page':'about'}
    return render(request,'first/about.html',context)

def homefun(request):
    context = {'page':'home'}
    return render(request,'first/home.html',context)

def success_page(request):
    print("*"*10)
    return HttpResponse("<h1>hi this is success page</h1>")
