from django.http import HttpResponse
from .models import Cryptid, Location
from django.shortcuts import render

# def index(request):
#     questions = Question.objects.all()
#     qs = ", ".join([q.question_text for q in questions]) 
#     return HttpResponse(qs)

def detail(request, cryptid_id):
    monster = Cryptid.objects.get(pk=cryptid_id) 
    return HttpResponse(monster.name)

def bio(request, cryptid_id):
    context = {"cryptid": Cryptid.objects.get(pk=cryptid_id)} 
    return render(request, "polls/bio.html", context)

def locations(request):
    context = {"locations": Location.objects.all()}
    return render(request, "polls/locations.html", context)

def location(request, location_id):
    context = {"location": Location.objects.get(pk=location_id)}
    return render(request, "polls/location.html", context)


def index(request):
    context = {"cryptids": Cryptid.objects.all()} 
    return render(request, "polls/index.html", context)

 

