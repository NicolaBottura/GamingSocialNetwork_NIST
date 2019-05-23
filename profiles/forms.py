from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from profiles.models import UserProfile
from profiles.riot import find_my_rank


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        #user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):

    class Meta:
        model = UserProfile
        fields = {
            'game_tag',
            'region',
        }


class GetRankForm(UserChangeForm):

    class Meta:
        model = UserProfile
        fields = {
            'ranked_flex',
            'ranked_solo_tier',
            'ranked_solo_rank',
            'ranked_solo_points'
        }

    """
    def save(self, commit=True):
        game_stats = super(GetRankForm, self).save(commit=False)
        game_stats.ranked_flex = self.cleaned_data['ranked_flex']
        game_stats.ranked_solo_tier = self.cleaned_data['ranked_solo_tier']
        game_stats.ranked_solo_rank = self.cleaned_data['ranked_solo_rank']
        game_stats.ranked_solo_points = self.cleaned_data['ranked_solo_points']

        if commit:
            game_stats.save()

        return game_stats
    """