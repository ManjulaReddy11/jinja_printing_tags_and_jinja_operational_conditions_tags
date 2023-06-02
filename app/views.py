from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'ASHU'}
    return render(request,'wish.html',context=d)

def conditions(request):
    c={'a':10,'b':20,'c':30}
    return render(request,'conditions.html',context=c)

def loop(request):
    m={'name':'MANJU'}
    return render(request,'loop.html',m)
