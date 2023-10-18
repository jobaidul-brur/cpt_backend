from django.urls import path

from . import views

urlpatterns = [
    path('parse/', views.parse_problem, name='parse'),
]
