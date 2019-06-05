# In questo file faccio in modo che ad un utente non loggato
# non possa vedere altro se non la template di login, in modo da aumentare la sicurezza.

import re
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.urls import reverse

# porta dentro tutti gli url definiti nel file ../settings
# da EXEMPT_URLS
EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')

        # lstrip per rimuovere lo '/' iniziale negli urls
        path = request.path_info.lstrip('/')

        url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)

        if path == reverse('profiles:logout').lstrip('/'):
            LogoutView.as_view(template_name='auth/logout.html')

        if request.user.is_authenticated and url_is_exempt:
            return redirect(settings.LOGIN_REDIRECT_URL)
        elif request.user.is_authenticated or url_is_exempt:
            return None
        else:
            return redirect(settings.LOGIN_URL)
