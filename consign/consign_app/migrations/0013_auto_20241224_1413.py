# Generated by Django 3.0 on 2024-12-24 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0012_auto_20241224_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='addconsignment',
            name='actualweight',
            field=models.FloatField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='addconsignment',
            name='dlno',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='addconsignment',
            name='methodpkg',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
