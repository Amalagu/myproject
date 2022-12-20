from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Image
# Create your views here.

def indexpage(request):
    imagescollections = Image.objects.all()
    fieldslist=[f.name for f in Image._meta._get_fields()]
    template= loader.get_template('myalbum.html')
    context = {
        'images' : imagescollections,
        'fieldslist': fieldslist
    }
    return HttpResponse(template.render(context, request))

def displaypage(request, id):
    image=Image.objects.get(id=id)
    fieldslist=[f.name for f in Image._meta._get_fields()]
    template = loader.get_template('display.html')
    context = {
        'image':image,
        'fieldslist': fieldslist
    }
    return HttpResponse(template.render(context, request))


def editpage(request, id):
    image=Image.objects.get(id=id)
    fieldslist=[f.name for f in Image._meta._get_fields()]
    template = loader.get_template('editpage.html')
    context = {
        'image':image,
        'fieldslist': fieldslist
    }
    return HttpResponse(template.render(context, request))

def commitchanges(request, id):
    image = Image.objects.get(id=id)
    image.title = request.POST['title']
    image.description= request.POST['description']
    image.owner = request.POST['owner']
    image.upload_time = request.POST['upload_time']
    image.annotated = request.POST['annotated']
    image.source = request.POST['source']
    image.modified = request.POST['modified']
    image.save()
    return HttpResponseRedirect(reverse('indexpage'))
