from django.shortcuts import redirect
from django.views import generic

from . import settings


def login_redirect(request):
    return redirect(settings.LOGIN_REDIRECT_URL)


class HomeView(generic.TemplateView):

    template_name = "../home/templates/home/home.html"
