# Generated by Django 4.1.3 on 2022-11-28 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_aipost_summary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aipost',
            name='questions',
        ),
    ]
