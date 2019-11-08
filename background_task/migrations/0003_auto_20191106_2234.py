# Generated by Django 2.2 on 2019-11-07 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('background_task', '0002_auto_20170927_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_group',
            field=models.CharField(db_index=True, default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='task',
            name='task_uid',
            field=models.CharField(db_index=True, default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='completedtask',
            name='task_group',
            field=models.CharField(db_index=True, default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='completedtask',
            name='task_uid',
            field=models.CharField(db_index=True, default=None, max_length=50),
        ),
    ]