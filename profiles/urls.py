from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', LoginView.as_view(template_name='profiles/login.html')),
    url(r'^logout/$', LogoutView.as_view(template_name='profiles/logout.html')),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
]