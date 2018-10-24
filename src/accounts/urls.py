from django.conf.urls import url
from django.contrib.auth.views import (login, logout, logout_then_login, password_reset, password_reset_confirm, password_reset_done,    password_reset_confirm, password_reset_complete, password_change, password_change_done)

from . import views


urlpatterns = [
    #login/logout urls
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout' ),
    url(r'^logout-then-logout/$', logout_then_login, name='logout_then_login'),

    # change password urls
    url(r'^password-change/$','django.contrib.auth.views.password_change',name='password_change'),
    url(r'^password-change/done/$','django.contrib.auth.views.password_change_done',name='password_change_done'),

    # restore password urls
    url(r'^password-reset/$', 'password_reset',name='password_reset'),
    url(r'^password-reset/done/$', 'password_reset_done', name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$','password_reset_confirm', name='password_reset_confirm'),
    url(r'^password-reset/complete/$', 'password_reset_complete', name='password_reset_complete'),

    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^register/$', views.register, name='register')
]