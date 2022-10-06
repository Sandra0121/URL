from django.urls import path
from .views import index_view, create_view, go_view


urlpatterns = [
    path('', index_view, name='index'),
    path('create', create_view, name='create'),
    path('<str:pk>', go_view, name='go'),
]