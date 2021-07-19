from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Main.as_view()),
    path('skins/', views.Show.as_view())
]