from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('reports/', views.reports, name='reports'),
    path('add_member/', views.add_member, name='add_member'),
    path('update_member/<int:pk>', views.update_member, name='update_member'),
    path('member_details/<int:pk>', views.member_details, name='member_details'),
    path('delete_member/<int:pk>', views.delete_member, name='delete_member'),
    path('add_payment/<int:pk>', views.add_payment, name='add_payment'),

    
]
