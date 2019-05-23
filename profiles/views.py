from django.shortcuts import render, redirect, HttpResponseRedirect
from profiles.forms import SignupForm, EditProfileForm, GetRankForm
from profiles.riot import find_my_rank


def home(request):
    numbers = {1,2,3,4,5}
    name = 'Nicola Bottura'

    args = {'myName': name, 'myNumbers': numbers}
    return render(request, 'profiles/home.html', args)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/profiles')
    else:
        form = SignupForm()

    args = {'form': form}
    return render(request, 'profiles/signup_form.html', args)


def view_profile(request):
    #find_my_rank()
    args = {'user': request.user}
    return render(request, 'profiles/profile.html', args)


def edit_profile(request):
    template_name = 'profiles/edit_profile.html'

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            #return redirect('/profiles/profile')

        find_my_rank(request)
        rank_update_form = GetRankForm(request.POST, instance=request.user.userprofile)
        print("son qui")
        if rank_update_form.is_valid():
            rank_update_form.save()
            return redirect('/profiles/profile')
        #else:
            #return render(request, 'profiles/edit_profile.html', {'form': form, 'rank_form': rank_update_form})
    else:
        form = EditProfileForm(instance=request.user.userprofile)
        rank_update_form = GetRankForm(instance=request.user.userprofile)

        args = {'form': form, 'rank_form': rank_update_form}
        return render(request, template_name, args)
