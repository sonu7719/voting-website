# Generated by Django 5.0 on 2024-03-30 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting_home', '0006_rename_contact_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='Phone_no',
            new_name='Age',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='Last_name',
        ),
    ]
