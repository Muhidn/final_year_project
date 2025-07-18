from rest_framework import serializers
from .models import User, School, School_Admin, Request

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
            'password': {'write_only': True, 'required': False},
            'username': {'validators': []},
            'email': {'validators': []},
        }

    def validate_username(self, value):
        user = self.instance
        if user and user.username == value:
            return value
        if User.objects.filter(username=value).exclude(pk=user.pk if user else None).exists():
            raise serializers.ValidationError('user with this username already exists.')
        return value

    def validate_email(self, value):
        user = self.instance
        if user and user.email == value:
            return value
        if User.objects.filter(email=value).exclude(pk=user.pk if user else None).exists():
            raise serializers.ValidationError('user with this email already exists.')
        return value

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            if attr in ['username', 'email']:
                if value and getattr(instance, attr) != value:
                    setattr(instance, attr, value)
            else:
                setattr(instance, attr, value)
        if password:
            instance.password = password  # Or use set_password if using Django auth
        instance.save()
        return instance

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'address', 'phone_number', 'email']

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

class SchoolAdminSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())

    class Meta:
        model = School_Admin
        fields = ['id', 'user', 'school']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        school_admin = School_Admin.objects.create(user=user, **validated_data)
        return school_admin


class RequestUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'phone_number']


class RequestSerializer(serializers.ModelSerializer):
    user = RequestUserSerializer(read_only=True)
    school = serializers.PrimaryKeyRelatedField(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    school_id = serializers.IntegerField(write_only=True)
    requested_at = serializers.DateTimeField(source='created_at', read_only=True)
    
    class Meta:
        model = Request
        fields = ['id', 'user', 'school', 'user_id', 'school_id', 'status', 'requested_at']
        
    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        school_id = validated_data.pop('school_id')
        user = User.objects.get(id=user_id)
        school = School.objects.get(id=school_id)
        return Request.objects.create(user=user, school=school, **validated_data)
        
    def update(self, instance, validated_data):
        user_id = validated_data.pop('user_id', None)
        school_id = validated_data.pop('school_id', None)
        
        if user_id:
            instance.user = User.objects.get(id=user_id)
        if school_id:
            instance.school = School.objects.get(id=school_id)
            
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
