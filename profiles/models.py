from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    country = models.CharField(max_length=15, blank=True)
    image = models.ImageField(upload_to='profile_images', default='profile_images/default.jpg')
    # game data below
    game_tag = models.CharField(max_length=15, default='')
    region = models.CharField(max_length=4, default='')
    ranked_flex = models.CharField(max_length=20, default='')
    wins_flex = models.CharField(max_length=4, default='')
    losses_flex = models.CharField(max_length=4, default='')
    ranked_solo = models.CharField(max_length=20, default='')
    wins_solo = models.CharField(max_length=4, default='')
    losses_solo = models.CharField(max_length=4, default='')

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
