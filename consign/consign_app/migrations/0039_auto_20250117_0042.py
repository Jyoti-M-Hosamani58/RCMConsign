# Generated by Django 3.0 on 2025-01-16 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0038_auto_20250117_0041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addconsignmenttemp',
            old_name='delivery',
            new_name='collection_type',
        ),
    ]
