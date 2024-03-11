from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/create/', views.room_create, name='create_room'),
    path('rooms/join/', views.join_room, name='join_room'),
    path('rooms/<slug:slug>/', views.room_detail, name='room_detail'),
    path('rooms/<slug:room_slug>/messages/', views.message_list, name='message_list'),
    path('rooms/<slug:room_slug>/new_message/', views.new_message, name='new_message'),
    
]
