# Generated by Django 3.2.8 on 2023-02-24 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_todouser_birthday_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todouser',
            name='user_name',
            field=models.CharField(max_length=64),
        ),
    ]
