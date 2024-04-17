import urllib.request
from django.shortcuts import render,HttpResponse
import requests
import webbrowser

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about_us.html')

def add_notes(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        location = request.POST.get('location')
        filename = request.POST.get('filename')
        if filename == None:
            return HttpResponse("Enter a valid filename")
        if not location== 'static':
            location=None
        if location == None:
            location='static/uploads/' + filename
        else:
            location = 'static/'+location + '/' + filename
        with open(location, 'w') as f:
            f.write(text)
        return HttpResponse("Note added")
    return render(request,'add_notes.html')

def robots(request):
    return render(request,'robots.html')

def post_notes(request):
    if request.method == 'POST':
        with open("flag.txt", 'r') as f:
            flag = f.read()
        web_url = request.POST.get('web_url')
        location = request.POST.get('location')
        filename = request.POST.get('filename')
        if filename == None:
            return HttpResponse("Enter a valid filename")
        url=web_url+'/static/'+location+'/'+filename
        if not (url.startswith('http://127.0.0.1:8000/static/static') or url.startswith('http://127.0.0.1:8000//static/static')):
            return HttpResponse("Location of flag is different")
        return HttpResponse(f"Visited link successfully\nHere is your flag:{flag}")
    return render(request,'post_notes.html')