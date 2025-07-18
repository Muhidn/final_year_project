from django.shortcuts import render
from rest_framework import generics
from .models import Student, Lecture, Attendance
from .serializers import StudentSerializer, LectureSerializer, AttendanceSerializer

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

studentListCreateView = StudentListCreateView.as_view()

class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
studentRetrieveUpdateDestroyView = StudentRetrieveUpdateDestroyView.as_view()

class LectureListCreateView(generics.ListCreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer

lectureListCreateView = LectureListCreateView.as_view()

class LectureRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer

lectureRetrieveUpdateDestroyView = LectureRetrieveUpdateDestroyView.as_view()

class AttendanceListCreateView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

attendanceListCreateView = AttendanceListCreateView.as_view()

class AttendanceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

attendanceRetrieveUpdateDestroyView = AttendanceRetrieveUpdateDestroyView.as_view()

