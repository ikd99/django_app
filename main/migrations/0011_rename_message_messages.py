# Generated by Django 3.2.7 on 2021-10-08 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20211007_1046'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='message',
            new_name='messages',
        ),
    ]
