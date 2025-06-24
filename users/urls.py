from django.urls import path
from .views import (
    userListCreateView, userRetrieveUpdateDestroyView,
    schoolListCreateView, schoolRetrieveUpdateDestroyView,
    schoolAdminListCreateView, schoolAdminRetrieveUpdateDestroyView,
    loginView
)

urlpatterns = [
    path('users/', userListCreateView, name='user-list-create'),
    path('users/<int:pk>/', userRetrieveUpdateDestroyView, name='user-detail'),
    path('schools/', schoolListCreateView, name='school-list-create'),
    path('schools/<int:pk>/', schoolRetrieveUpdateDestroyView, name='school-detail'),
    path('school_admins/', schoolAdminListCreateView, name='school-admin-list-create'),
    path('school_admins/<int:pk>/', schoolAdminRetrieveUpdateDestroyView, name='school-admin-detail'),
    path('login/', loginView, name='login'),
]
