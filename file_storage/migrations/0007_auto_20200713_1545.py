# Generated by Django 3.0.7 on 2020-07-13 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_storage', '0006_userfile_countdown'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfile',
            name='countdown',
            field=models.CharField(max_length=100),
        ),
    ]
