from django.shortcuts import render
from .models import contact_info
# Create your views here.
def about(request):
     context = {}
     return render(request, 'pages/about.html', context)

def blog(request):
     context = {}
     return render(request, 'pages/blog.html', context)

def case_details(request):
      context = {}
      return render(request, 'pages/Case_details.html', context)

def case_study(request):
     context = {}
     return render(request, 'pages/Case_Study.html', context)

def contact(request):
     context = {}
     return render(request, 'pages/contact.html', context)

def submitted_contact(request):
    message = request.POST['message']
    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']

    details = contact_info(message=message, name=name, email=email, subject=subject)
    details.save()
    return render(request, 'pages/contact.html')

def elements(request):
      context = {}
      return render(request, 'pages/elements.html', context)

def index(request):
     context = {}
     return render(request, 'pages/index.html', context )

def services(request):
     context = {}
     return render(request, 'pages/services.html', context)

def single_blog(request):
      context = {}
      return render(request, 'pages/single_blog.html', context)	  
