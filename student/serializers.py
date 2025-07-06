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
            # Manually update user fields to avoid validation issues
            user = instance.user
            for attr, value in user_data.items():
                if attr == 'password' and value:
                    user.set_password(value)
                elif attr in ['username', 'email']:
                    # Only update if the value is actually different
                    if getattr(user, attr) != value:
                        # Check for uniqueness manually
                        from users.models import User
                        if User.objects.filter(**{attr: value}).exclude(pk=user.pk).exists():
                            raise serializers.ValidationError({
                                'user': {attr: [f'user with this {attr} already exists.']}
                            })
                        setattr(user, attr, value)
                else:
                    setattr(user, attr, value)
            user.save()
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

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
