# Generated by Django 3.0 on 2025-01-18 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0043_auto_20250118_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lcm',
            name='addconsignment',
        ),
        migrations.AddField(
            model_name='lcm',
            name='consignment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='consign_app.AddConsignment'),
        ),
    ]
