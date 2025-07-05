from django.db import models
from users.models import User, School

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students', blank=True, null=True)

    form = models.FileField(upload_to='student_forms/', blank=True, null=True)
    permit = models.FileField(upload_to='student_permits/', blank=True, null=True)
    theory_result = models.CharField(max_length=40, choices=[('pass', 'Pass'), ('fail', 'Fail'), ('pending', 'Pending')], default='pending')
    practical_result = models.CharField(max_length=40, choices=[('pass', 'Pass'), ('fail', 'Fail'), ('pending', 'Pending')], default='pending')
    updated_at = models.DateTimeField(auto_now=True)
    document = models.FileField(upload_to='student_documents/', blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name()


    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        # If no file is uploaded, set form and permit to 'pending' (string)
        if not self.form:
            self.form = None  # FileField must be None if no file
        if not self.permit:
            self.permit = None
        super().save(*args, **kwargs)

class Lecture(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='lecture_profile')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='lectures', blank=True, null=True)
    license_class = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.license_class}"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=[('present', 'Present'), ('absent', 'Absent')],
        default='present'
    )

    def __str__(self):
        return f"{self.student.user.username} - {self.lecture.license_class} on {self.date} ({self.status})"

    class Meta:
        unique_together = ('student', 'lecture', 'date')

class Message(models.Model):
    body = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='messages')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='messages')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message to {self.student} at {self.school}: {self.body[:30]}"

class Notification(models.Model):
    body = models.TextField()
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='notifications')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.school}: {self.body[:30]}"



