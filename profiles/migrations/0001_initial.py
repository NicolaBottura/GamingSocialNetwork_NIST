# Generated by Django 2.1.4 on 2019-06-17 19:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=100)),
                ('country', models.CharField(blank=True, max_length=15)),
                ('image', models.ImageField(default='profile_images/default.jpg', upload_to='profile_images')),
                ('game_tag', models.CharField(default='', max_length=15)),
                ('region', models.CharField(default='', max_length=4)),
                ('ranked_flex', models.CharField(default='', max_length=20)),
                ('wins_flex', models.CharField(default='', max_length=4)),
                ('losses_flex', models.CharField(default='', max_length=4)),
                ('ranked_solo', models.CharField(default='', max_length=20)),
                ('wins_solo', models.CharField(default='', max_length=4)),
                ('losses_solo', models.CharField(default='', max_length=4)),
                ('user', models.OneToOneField(on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
