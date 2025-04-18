
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('create/', views.create_character, name='create_character'),
    path('interview/<int:character_id>/', views.interview, name='interview'),
]

