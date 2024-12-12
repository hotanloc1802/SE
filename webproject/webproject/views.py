from django.shortcuts import render
def tranchu(request):
    return render(request, 'trangchu.html')  # Ensure this matches the template name

def vechungto(request):
    return render(request, 'vechungto.html') 

def bosuutap(request):
    return render(request, 'bosuutap.html') 

def workshop(request):
    return render(request, 'workshop.html') 

def installation(request):
    return render(request, 'installation.html') 
