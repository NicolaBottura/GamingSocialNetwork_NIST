from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete='CASCADE')
    description = models.CharField(max_length=100, default='')
    game_tag = models.CharField(max_length=100, default='')
    region = models.CharField(max_length=100, default='')
    ranked_flex = models.CharField(max_length=100, default='')
    ranked_solo_tier = models.CharField(max_length=100, default='')
    ranked_solo_rank = models.CharField(max_length=100, default='')
    ranked_solo_points = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
