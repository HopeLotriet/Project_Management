# Generated by Django 5.2 on 2025-05-25 18:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0003_supervisorprofile_supervisorfeedback'),
        ('projects', '0007_chatmessage_meeting'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='supervisor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='adminpanel.supervisorprofile'),
        ),
    ]
