"""
Per quanto riguarda la modifica delle password, diamo all'utente due diversi metodi.
Il primo modo, quello a cui vi su puo' accedere tramite l'url 'profile/edit/change-password',
ci permette di modificare la password nel caso in cui ci ricordiamo ancora di quella vecchia.
Il secondo metodo invece, quello che parte da 'reset-password', ci permette di modificare la password
di un account nel caso in cui non riusciamo a ricordarci quella vecchia.
Per fare cio' sara' necessario conoscere la mail dell'utente in questione e di conseguenza
utilizziamo un server mail per servirci di questa funzionalita' che andremo ad attivare
scrivendo questo comando in un terminale:
    python -m smtpd -n -c DebuggingServer localhost:1025
Sul terminale, vederemo in output una mail con diverse informazioni, tra cui un link ad una pagina
la quale ci permettera' di resettare la nostra password.
"""
from django.conf.urls import url
from . import views
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

app_name = 'profiles'


urlpatterns = [
    url(r'^login/$', LoginView.as_view(template_name='auth/login.html'), name='login'), #as_view mi permette di convertire una classe in una funzione, che e' cio' che l'url resolver vuole
    url(r'^logout/$', LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profiles/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^profile/edit/change-password/$', views.change_password, name='change_password'),
    url(r'^reset-password/$', PasswordResetView.as_view(template_name=
        'edit_password/reset_password.html', success_url='done/',
                                                        email_template_name='edit_password/reset_password_email.html'),
        name='reset_password'),
    url(r'^reset-password/done/$', PasswordResetDoneView.as_view(
        template_name='edit_password/reset_password_done.html'), name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        PasswordResetConfirmView.as_view(template_name='edit_password/reset_password_confirm.html',
        success_url='/profiles/reset-password/complete/'),
        name='password_reset_confirm'),
    url(r'^reset-password/complete/$', PasswordResetCompleteView.as_view(template_name=
        'edit_password/reset_password_complete.html'), name='password_reset_complete')
]