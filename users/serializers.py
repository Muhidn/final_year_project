from rest_framework import serializers
from .models import User, School, School_Admin

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'is_active',
            'date_joined',
            'role',
            'address',
            'phone_number',
            'profile_picture',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'address', 'phone_number', 'email']

class SchoolAdminSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    school = SchoolSerializer(required=False, allow_null=True)
    class Meta:
        model = School_Admin
        fields = ['id', 'user', 'school']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid credentials')
        if not user.is_active:
            raise serializers.ValidationError('User is inactive')
        if user.password != password:
            raise serializers.ValidationError('Invalid credentials')
        data['user'] = user
        return data
