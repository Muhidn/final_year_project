from rest_framework import serializers
from .models import Student, Lecture, Attendance, Message, Notification

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id',
            'user',
            'school',
            'form',
            'permit',
            'theory_result',
            'practical_result',
            'updated_at',
            'document',
        ]

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['id', 'user', 'school', 'license_class']

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'student', 'lecture', 'date', 'status']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'body', 'student', 'school', 'created_at']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'body', 'school', 'created_at']
