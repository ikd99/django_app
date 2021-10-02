# Generated by Django 3.2.7 on 2021-10-02 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211002_0641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='user_id',
        ),
        migrations.AddField(
            model_name='request',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user_info'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.request'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user_info'),
        ),
        migrations.AlterField(
            model_name='message',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.request'),
        ),
        migrations.AlterField(
            model_name='message',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.user_info'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.request'),
        ),
    ]
