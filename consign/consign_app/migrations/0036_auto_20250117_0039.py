# Generated by Django 3.0 on 2025-01-16 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0035_auto_20250117_0038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addconsignmenttemp',
            old_name='balance',
            new_name='otherCharge',
        ),
    ]
