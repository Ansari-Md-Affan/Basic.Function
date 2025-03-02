#from http.client import HTTPResponse

# Create your views here.
from django.shortcuts import render,HttpResponse
def index(request):
    return render(request,'index.html')

def analyzed(request):
    text = request.POST.get('text', "off")
    removepunc = request.POST.get('removepunc', "off")
    spaceremove = request.POST.get('spaceremove', "off")
    removeline = request.POST.get('removeline', "off")
    upper = request.POST.get('upper', "off")
    if removepunc=="on":
        punc = '''.,?!:;'"()-–—…[]/&^<>'~\''''
        analytext = ""
        for char in text:
            if char not in punc:
                analytext += char
        text = analytext
    if spaceremove == "on":
        analytext =""
        for i,char in enumerate(text):
            if text[i]==" "and text[i+1]==" ":
                pass
            else:
                analytext=analytext+char
        text = analytext
    if upper == "on":
        analytext=""
        for char in text:
            analytext =analytext+char.upper()
        text = analytext
    if removeline=="on":
        analytext=""
        for char in text:
            if char!="\n" and char!="\r":
                analytext = analytext + char

        text = analytext
    hi={
        "texthere":text
    }
    if removepunc!="on" and spaceremove!="on" and upper!="on" and removeline!="on":
        return HttpResponse("Error")
    return render(request,"analyzed.html",hi)
def link(request):
    return HttpResponse(''' <h1>Some link important for student</h1>
    django playlist   <a href="https://www.youtube.com/watch?v=JxzZxdht-XY">Click Here</a><br>
    sppu Result   <a href="https://onlineresults.unipune.ac.in/Result/Dashboard/Default">Click Here</a><br>
    MAHADBT login link   <a href="https://testdbtapp.mahaitgov.in/Login/Login">Click Here</a><br>''')