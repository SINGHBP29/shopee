# Generated by Django 4.1.7 on 2023-03-12 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dell', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='login',
            new_name='loginForm',
        ),
        migrations.RenameModel(
            old_name='registration',
            new_name='registrationForm',
        ),
    ]
