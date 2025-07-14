from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import User, School, School_Admin, Request
from .serializers import UserSerializer, SchoolSerializer, LoginSerializer, SchoolAdminSerializer, RequestSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

userListCreateView = UserListCreateView.as_view()

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
userRetrieveUpdateDestroyView = UserRetrieveUpdateDestroyView.as_view()

class SchoolListCreateView(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

schoolListCreateView = SchoolListCreateView.as_view()

class SchoolRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

schoolRetrieveUpdateDestroyView = SchoolRetrieveUpdateDestroyView.as_view()

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user_data = UserSerializer(user).data
        return Response(user_data, status=status.HTTP_200_OK)

loginView = LoginView.as_view()

class SchoolAdminListCreateView(generics.ListCreateAPIView):
    queryset = School_Admin.objects.all()
    serializer_class = SchoolAdminSerializer

schoolAdminListCreateView = SchoolAdminListCreateView.as_view()

class SchoolAdminRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = School_Admin.objects.all()
    serializer_class = SchoolAdminSerializer

schoolAdminRetrieveUpdateDestroyView = SchoolAdminRetrieveUpdateDestroyView.as_view()


class RequestListCreateView(generics.ListCreateAPIView):
    queryset = Request.objects.select_related('user', 'school').all()
    serializer_class = RequestSerializer

requestListCreateView = RequestListCreateView.as_view()

class RequestRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.select_related('user', 'school').all()
    serializer_class = RequestSerializer

requestRetrieveUpdateDestroyView = RequestRetrieveUpdateDestroyView.as_view()
# Create your views here.
