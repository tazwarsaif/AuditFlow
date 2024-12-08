# Generated by Django 5.1.3 on 2024-12-07 15:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_appointmentreschedulerequest'),
        ('core', '0002_auditor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='assigned_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auditor_appointments', to='core.auditor'),
        ),
    ]