# Generated by Django 4.1.3 on 2022-11-28 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_openai_aipost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aipost',
            name='summary',
        ),
    ]
