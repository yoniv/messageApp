from django.urls import path, include

from messages_api import views


app_name = 'messageApp_api'
urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('get_all_messages/', views.get_all_messages, name='get_all_messages'),
    path('get_all_sent_messages/', views.get_all_sent_messages, name='get_all_sent_messages'),
    path('get_all_unread_messages/', views.get_all_unread_messages, name='get_all_unread_messages'),
    path('get_message/', views.get_message, name='get_message'),
    path('create_message/', views.create_message, name='create_message'),
    path('delete_message/', views.delete_message, name='delete_message'),
]