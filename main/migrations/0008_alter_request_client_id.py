# Generated by Django 3.2.7 on 2021-10-02 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_request_client_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='client_id',
            field=models.IntegerField(),
        ),
    ]
