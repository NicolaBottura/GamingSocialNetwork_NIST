from django.shortcuts import render, redirect, HttpResponseRedirect
from profiles.forms import SignupForm, EditProfileForm, EditCustomFieldsForm
from profiles.riot import find_my_rank
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import User, UserProfile


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


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user

    args = {'user': user}
    return render(request, 'profiles/profile.html', args)


def edit_profile(request):
    template_name = 'profiles/edit_profile.html'

    if request.method == 'POST':
        form = EditCustomFieldsForm(request.POST, instance=request.user.userprofile)
        form2 = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            find_my_rank(request)
            return redirect('/profiles/profile')
    else:
        form = EditCustomFieldsForm(instance=request.user.userprofile)
        form2 = EditProfileForm(instance=request.user)
        args = {'form': form, 'form2': form2}

        return render(request, template_name, args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            # mantiene la pagina nonostante abbia cambiato la password(non mi slogga)
            update_session_auth_hash(request, form.user)

            return redirect('/profiles/profile')
        else:
            return redirect('profiles/change-password')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}

        return render(request, 'edit_password/change_password.html', args)


def search_bar(request):
    if request.method == 'GET':
        search_query = request.GET.get('search')
        user = User.objects.get(user=search_query)

        query = user.filter(user__icontains=search_query)

        args = {'user': query}

        return redirect(request, 'profiles/profile.html', args)

