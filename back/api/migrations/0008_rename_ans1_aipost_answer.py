# Generated by Django 4.1.3 on 2023-01-02 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_aipost_ans1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aipost',
            old_name='ans1',
            new_name='answer',
        ),
    ]
