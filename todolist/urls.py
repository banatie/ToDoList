from django.urls import include, path

from . import views

app_name = 'todolist'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('todo/add', views.add_todo, name='add_todo'),
    path('<int:todo_id>/delete', views.delete_todo, name='delete_todo'),
]