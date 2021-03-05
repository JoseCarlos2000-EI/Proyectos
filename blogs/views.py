from django.shortcuts import render,HttpResponse
from .models import persona,Conocimiento
# Create your views here.
def portafolio(request):
    return render(request,"index.html")

def about(request):
    arrayu=persona.objects.first()
    arrayc=Conocimiento.objects.all()
    return render(request,"about.html",{'usuario':arrayu,'cono':arrayc})

def contact(request):
    arrayu=persona.objects.first()
    return render(request,"contact.html",{'usuario':arrayu})