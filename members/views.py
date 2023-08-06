from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member, Car

# Create your views here.

def members(request):
    # return HttpResponse("Hello World!")
    mymembers = Member.objects.all().values()
    template = loader.get_template('allmembers.html')
    context = {
        'mymembers' : mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def cars(request):
    mycars = Car.objects.all().values()
    template = loader.get_template('cars.html')
    context = {
        'futurecars' : mycars
        
    }
    return HttpResponse(template.render(context, request))

def cardetails(request, id):
    mycar = Car.objects.get(id=id)
    template = loader.get_template('car-details.html')
    context = {
        'mycar' : mycar
    }
    return HttpResponse(template.render(context, request))
    