# Generated by Django 3.0.6 on 2021-01-07 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yogbookingapp', '0009_auto_20210107_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='dob',
        ),
    ]
