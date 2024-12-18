# Generated by Django 5.1.3 on 2024-12-14 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auditor'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditor',
            name='current_location',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='auditor',
            name='status',
            field=models.CharField(choices=[('ONLINE', 'ONLINE'), ('ON THE WAY', 'ON THE WAY'), ('OFFLINE', 'OFFLINE')], default='OFFLINE', max_length=20),
        ),
    ]
