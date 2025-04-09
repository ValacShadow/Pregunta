from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('feed/', views.question_list, name='question_list'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('ask/', views.ask_question, name='ask_question'),
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('question/<int:pk>/answer/', views.answer_question, name='answer_question'),
    path('answer/<int:pk>/like/', views.like_answer, name='like_answer'),
]
