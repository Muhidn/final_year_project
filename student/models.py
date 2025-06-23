from django.db import models
from users.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    form = models.FileField(upload_to='student_forms/', blank=True, null=True)
    permit = models.FileField(upload_to='student_permits/', blank=True, null=True)
    theory_result = models.CharField(max_length=4, choices=[('pass', 'Pass'), ('fail', 'Fail')])
    practical_result = models.CharField(max_length=4, choices=[('pass', 'Pass'), ('fail', 'Fail')])
    updated_at = models.DateTimeField(auto_now=True)
    document = models.FileField(upload_to='student_documents/', blank=True, null=True)

    def __str__(self):
        return self.user.username
# Create your models here.
