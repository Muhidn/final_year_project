# Generated by Django 4.2.23 on 2025-07-03 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_school_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school_admin',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='school_admins', to='users.school'),
        ),
    ]
