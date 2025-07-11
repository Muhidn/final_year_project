# Generated by Django 4.2.23 on 2025-06-23 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form', models.FileField(blank=True, null=True, upload_to='student_forms/')),
                ('permit', models.FileField(blank=True, null=True, upload_to='student_permits/')),
                ('theory_result', models.CharField(choices=[('pass', 'Pass'), ('fail', 'Fail')], max_length=4)),
                ('practical_result', models.CharField(choices=[('pass', 'Pass'), ('fail', 'Fail')], max_length=4)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('document', models.FileField(blank=True, null=True, upload_to='student_documents/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_profile', to='users.user')),
            ],
        ),
    ]
