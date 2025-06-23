from django.shortcuts import render
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

studentListCreateView = StudentListCreateView.as_view()

class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
studentRetrieveUpdateDestroyView = StudentRetrieveUpdateDestroyView.as_view()

# Create your views here.
