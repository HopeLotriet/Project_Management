# Generated by Django 5.2 on 2025-05-23 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('manager', 'Project Manager'), ('staff', 'Staff'), ('student', 'Student')], default='staff', max_length=10),
        ),
    ]
