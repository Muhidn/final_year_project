from django.urls import path
from .views import userListCreateView, userRetrieveUpdateDestroyView

urlpatterns = [
    path('users/', userListCreateView, name='user-list-create'),
    path('users/<int:pk>/', userRetrieveUpdateDestroyView, name='user-detail'),
]
