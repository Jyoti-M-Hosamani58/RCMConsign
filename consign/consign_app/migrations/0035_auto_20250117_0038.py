# Generated by Django 3.0 on 2025-01-16 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0034_auto_20250117_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='addconsignmenttemp',
            name='receiver_email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='addconsignmenttemp',
            name='sender_email',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
