# Generated by Django 2.2 on 2019-06-07 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20190607_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='game_tag',
            field=models.CharField(default='', max_length=15),
        ),
    ]
