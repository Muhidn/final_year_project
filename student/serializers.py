from rest_framework import serializers
from .models import Student, Lecture, Attendance, Message, Notification
from users.serializers import UserSerializer

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

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

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        from users.models import User
        user = User.objects.create(**user_data)
        student = Student.objects.create(user=user, **validated_data)
        return student

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user = instance.user
            # Prevent updating username and email
            user_data.pop('username', None)
            user_data.pop('email', None)
            for attr, value in user_data.items():
                if attr == 'password' and value:
                    user.set_password(value)
                elif attr != 'password':
                    setattr(user, attr, value)
            user.save()
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def validate(self, data):
        user_data = data.get('user')
        if user_data and self.instance:
            user = self.instance.user
            username = user_data.get('username')
            if username and username != user.username:
                from users.models import User
                if User.objects.filter(username=username).exclude(pk=user.pk).exists():
                    raise serializers.ValidationError({'user': {'username': ['user with this username already exists.']}})
            email = user_data.get('email')
            if email and email != user.email:
                from users.models import User
                if User.objects.filter(email=email).exclude(pk=user.pk).exists():
                    raise serializers.ValidationError({'user': {'email': ['user with this email already exists.']}})
        return data

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
