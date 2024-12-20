# Generated by Django 5.1.3 on 2024-12-09 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='taskCategory',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='task',
            name='taskOwner',
            field=models.CharField(default='admin', max_length=255),
        ),
        migrations.AddField(
            model_name='task',
            name='taskScheduledFor',
            field=models.DateField(default='2024-12-09'),
        ),
        migrations.AlterField(
            model_name='task',
            name='taskName',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
