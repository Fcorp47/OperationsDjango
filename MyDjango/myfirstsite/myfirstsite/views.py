#this file created by arjun
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'Arjun','age':'22'}
    return render(request,'index.html',params)
    # return HttpResponse("arjun ka page")

def display(request):
    x = request.POST.get('textn')
    rmpunc = request.POST.get('punc','off')
    upcase = request.POST.get('caps','off')
    newlinerem = request.POST.get('newline','off')
    extraspace = request.POST.get('exspace','off')
    punc = '''{}.,/?[]'"'''
    temp = ""
    if(rmpunc == "on"):
        for char in x:
            if char not in punc:
                temp = temp + char
        x = temp;
    if(upcase=="on"):
        babe = x.upper()
        x = babe

    if(newlinerem=="on"):
        temp=""
        for char in x:
            if char!="\n":
                temp = temp + char
        x = temp
    if(extraspace=="on"):
        temp=""
        for index, char in enumerate(x):
            if not(x[index] == " " and x[index+1]==" "):
                temp = temp + char
        x = temp

    param = {'x':x}
    return render(request,'proc.html',param)


