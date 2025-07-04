# Generated by Django 4.2.23 on 2025-06-23 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('role', models.CharField(choices=[('zartsa', 'Zartsa'), ('school', 'School'), ('student', 'Student'), ('lecture', 'Lecture')], max_length=50)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
            ],
        ),
    ]
