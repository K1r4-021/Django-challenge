from django.shortcuts import render,HttpResponse
import webbrowser,requests
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
        if location=="static/" or location=="static":
            return HttpResponse("Trying XSS let me help you\nI am striping something more static")
        location=location.replace('static','',1)    
        if location == None:
            location = 'uploads/'
        with open(location+filename, 'w') as f:
            f.write(text)
        return HttpResponse("Note added")
    return render(request,'add_notes.html')

def robots(request):
    return render(request,'robots.html')

def admin_bot(request):
    if request.method == 'POST':
        with open("flag.txt", 'r') as f:
            flag = f.read()
        # webbrowser.open_new_tab('https://k1r4.pythonanywhere.com/static/exploit.html?flag='+flag)
        web_url = request.POST.get('web_url')
        if not (web_url.startswith('https://k1r4.pythonanywhere.com/') or web_url.startswith('http://127.0.0.1:8000/') ):
            return HttpResponse('Invalid URL')
        url = web_url + '?flag='+flag
        # return HttpResponse(r.text)
        r = requests.head(web_url)
        if not r.status_code == 200:
            return HttpResponse("Invalid location or file/directory not found")
        webbrowser.open_new_tab(url)  
        return HttpResponse(f"Visited link successfully")
    return render(request,'admin_bot.html')
