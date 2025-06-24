from django.urls import path
from .views import (
    StudentListCreateView, StudentRetrieveUpdateDestroyView,
    LectureListCreateView, LectureRetrieveUpdateDestroyView,
    AttendanceListCreateView, AttendanceRetrieveUpdateDestroyView
)

urlpatterns = [
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='student-detail'),
    path('lectures/', LectureListCreateView.as_view(), name='lecture-list-create'),
    path('lectures/<int:pk>/', LectureRetrieveUpdateDestroyView.as_view(), name='lecture-detail'),
    path('attendances/', AttendanceListCreateView.as_view(), name='attendance-list-create'),
    path('attendances/<int:pk>/', AttendanceRetrieveUpdateDestroyView.as_view(), name='attendance-detail'),
]
