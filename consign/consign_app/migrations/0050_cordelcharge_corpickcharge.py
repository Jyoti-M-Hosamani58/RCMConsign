# Generated by Django 3.0 on 2025-01-25 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0049_auto_20250122_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorDelcharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delPlace', models.CharField(max_length=500, null=True)),
                ('delrate', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CorPickcharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientName', models.CharField(max_length=500, null=True)),
                ('pickPlace', models.CharField(max_length=500, null=True)),
                ('clientId', models.IntegerField(max_length=500, null=True)),
                ('pickrate', models.FloatField(null=True)),
            ],
        ),
    ]
