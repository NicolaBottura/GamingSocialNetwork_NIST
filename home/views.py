from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from home.forms import HomeForm
from django.contrib.auth.models import User
from home.models import Post, Friend


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        # - davanti a created per stampare le date dalla piu' nuova alla piu vecchia
        posts = Post.objects.all().order_by('-created')
        users = User.objects.exclude(id=request.user.id)
        try:
            friend = Friend.objects.get(current_user=request.user)
            # friends list
            friends = friend.users.all()
        except Friend.DoesNotExist:
            friends = None

        args = {
            'form': form,
            'posts': posts,
            'users': users,
            'friends': friends
        }
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect('home:home')

        text = form.cleaned_data['post']
        form = HomeForm()
        args = {'form': form, 'text': text}

        return render(request, self.template_name, args)


def change_friends(request, operation, pk):
    new_friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, new_friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, new_friend)
    return redirect('home:home')



