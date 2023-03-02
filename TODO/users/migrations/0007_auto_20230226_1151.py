# Generated by Django 3.2.8 on 2023-02-26 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_todouser_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todouser',
            name='birthday_year',
        ),
        migrations.RemoveField(
            model_name='todouser',
            name='user_name',
        ),
        migrations.AlterField(
            model_name='todouser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='todouser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
