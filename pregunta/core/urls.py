from django.urls import path
from . import views

urlpatterns = [
    # Public/Home
    path('', views.home, name='home'),

    # Auth
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # User Pages
    path('account/', views.my_account, name='my_account'),
    path('questions/', views.my_questions, name='my_questions'),

    # Main Feed
    path('feed/', views.question_list, name='question_list'),
    path('ask/', views.ask_question, name='ask_question'),

    # Question Details
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('question/<int:pk>/answer/', views.answer_question, name='answer_question'),

    # Answer Actions
    path('answer/<int:pk>/like/', views.like_answer, name='like_answer'),
]
