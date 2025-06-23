from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id',
            'user',
            'form',
            'permit',
            'theory_result',
            'practical_result',
            'updated_at',
            'document',
        ]
