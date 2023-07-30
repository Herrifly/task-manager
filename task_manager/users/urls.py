from django.urls import path
from . import views
urlpatterns = [

    path('', views.register,  name='register'),
    path('auth/', views.auth, name='auth')


]