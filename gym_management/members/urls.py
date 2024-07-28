from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('reports/', views.reports, name='reports'),
    path('add_member/', views.add_member, name='add_member'),
]
