# Generated by Django 3.0 on 2024-12-26 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0015_auto_20241225_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addconsignment',
            old_name='dlno',
            new_name='collectionLocation',
        ),
        migrations.RenameField(
            model_name='addconsignmenttemp',
            old_name='dlno',
            new_name='accountHolder',
        ),
        migrations.AddField(
            model_name='addconsignment',
            name='collectionVehicleNo',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='addconsignment',
            name='dc',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='addconsignment',
            name='dcewaybill',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='addconsignment',
            name='dcno',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='addconsignment',
            name='dcvalue',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='addconsignment',
            name='desc',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='addconsignment',
            name='invoice',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='addconsignment',
            name='loadtype',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='addconsignment',
            name='receiver_email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='addconsignment',
            name='sender_email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='addconsignment',
            name='totalactalweight',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='addconsignment',
            name='totalpaidweight',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='addconsignment',
            name='totalpieces',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='addconsignmenttemp',
            name='dc',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='addconsignmenttemp',
            name='dcewaybill',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='addconsignmenttemp',
            name='dcno',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='addconsignmenttemp',
            name='dcvalue',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='addconsignmenttemp',
            name='desc',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='addconsignmenttemp',
            name='invoice',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='addconsignmenttemp',
            name='loadtype',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='addconsignmenttemp',
            name='totalactalweight',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='addconsignmenttemp',
            name='totalpaidweight',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='addconsignmenttemp',
            name='totalpieces',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
