from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Question, Answer, Like
from .forms import RegisterForm, QuestionForm, AnswerForm

def home(request):
    if request.user.is_authenticated:
        return redirect('question_list')

    top_questions = (
        Question.objects
        .annotate(total_likes=Count('answer__like'))
        .select_related('user')
        .order_by('-total_likes')[:10]
    )
    return render(request, 'home.html', {'questions': top_questions})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(request, username=uname, password=pwd)
        if user:
            login(request, user)
            return redirect('question_list')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def question_list(request):
    questions = (
        Question.objects
        .select_related('user')  # Fetch user for each question
        .order_by('-created_at')
    )
    return render(request, 'question_list.html', {'questions': questions})

@login_required
def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            q = form.save(commit=False)
            q.user = request.user
            q.save()
            return redirect('question_list')
    else:
        form = QuestionForm()
    return render(request, 'ask_question.html', {'form': form})

@login_required
def question_detail(request, pk):
    question = get_object_or_404(Question.objects.select_related('user'), pk=pk)

    answers = (
        Answer.objects
        .filter(question=question)
        .select_related('user', 'question')
        .prefetch_related('like_set')
        .annotate(num_likes=Count('like'))
        .order_by('-num_likes', '-created_at')
    )

    return render(request, 'question_detail.html', {'question': question, 'answers': answers})


@login_required
def answer_question(request, pk):
    question = get_object_or_404(Question.objects.select_related('user'), pk=pk)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            ans = form.save(commit=False)
            ans.user = request.user
            ans.question = question
            ans.save()
            return redirect('question_detail', pk=pk)
    else:
        form = AnswerForm()
    return render(request, 'answer_question.html', {'form': form, 'question': question})

@login_required
def like_answer(request, pk):
    answer = get_object_or_404(Answer.objects.select_related('question'), pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, answer=answer)
    return redirect('question_detail', pk=answer.question.id)
