# Generated by Django 3.0.7 on 2020-07-13 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_storage', '0004_userfile_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfile',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
    ]
