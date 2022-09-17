from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'myapp/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'myapp/question_detail.html', context)

@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(author=request.user, content=request.POST.get('content'), create_date=timezone.now())
    return redirect('detail', question_id=question_id)

@login_required(login_url='common:login')
def question_create(request):
    q = Question(author=request.user, subject=request.POST.get('subject'), content=request.POST.get('content'), create_date=timezone.now())
    q.save()
    return redirect('myapp:list')

@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'myapp/question_modify.html', context)

@login_required(login_url='common:login')
def question_modify_go(request):
    question = get_object_or_404(Question, pk=request.POST.get('id'))
    question.subject=request.POST.get('subject')
    question.content=request.POST.get('content')
    question.modify_date= timezone.now()
    question.save()
    return redirect('myapp:list')

@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return redirect('myapp:list')