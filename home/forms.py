from django import forms
from home.models import Post


class HomeForm(forms.ModelForm):
    post = forms.CharField()

    class Meta:
        model = Post
        # bisogna lasciare la virgola da sola per far capire
        # al compilatore che questa e' una tupla e non un intero.
        fields = {'post', }
