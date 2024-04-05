# Generated by Django 5.0 on 2024-03-23 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vote',
            fields=[
                ('Sr_no', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('vote', models.CharField(max_length=100)),
                ('party', models.CharField(choices=[('BJP', 'BJP'), ('Congress', 'Congress'), ('AAP', 'AAP'), ('others', 'Others (Specify Below)')], max_length=50)),
            ],
        ),
    ]
