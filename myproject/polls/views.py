from django.http import HttpResponse
from .models import Cryptid
from django.shortcuts import render

# def index(request):
#     questions = Question.objects.all()
#     qs = ", ".join([q.question_text for q in questions]) 
#     return HttpResponse(qs)

def detail(request, question_id):
    q = Cryptid.objects.get(pk=question_id) 
    return HttpResponse(q.question_text)

def index(request):
    context = {"cryptids": Cryptid.objects.all()} 
    return render(request, "polls/index.html", context)


