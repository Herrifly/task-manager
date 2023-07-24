from django.urls import path
from . import views
urlpatterns = [

    path('', views.index,  name='index'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/delete/<str:id>/', views.delete, name="delete")

]