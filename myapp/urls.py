from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='list'),
    path('<int:question_id>', views.detail, name='detail'),
    path('answer/create/<int:question_id>', views.answer_create, name='answer_create'),
    path('question/create', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>', views.question_modify, name='question_modify'),
    path('question/modify/go', views.question_modify_go, name='question_modify_go'),
    path('question/delete/<int:question_id>', views.question_delete, name='question_delete'),
]
