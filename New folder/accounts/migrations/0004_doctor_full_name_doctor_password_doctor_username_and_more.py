# Generated by Django 4.0.6 on 2022-11-07 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='full_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='username',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
