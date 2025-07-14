from django.db import models
class User(models.Model):
    STATUS_CHOICES = [
        ('student', 'Student'),
        ('lecture', 'Lecture'),
        ('super', 'Super'),
        ('admin', 'Admin'),
        ('school_admin', 'School_Admin'),
    ]

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=50, choices=STATUS_CHOICES)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.username
# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class School_Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='school_admin_profile')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='school_admins')

    def __str__(self):
        return self.user.username


class Request(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='requests', null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Request {self.id} - {self.user.username} ({self.status})"