# Generated by Django 2.2 on 2019-06-05 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20190529_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='losses_flex',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='losses_solo',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='wins_flex',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='wins_solo',
            field=models.CharField(default='', max_length=4),
        ),
    ]