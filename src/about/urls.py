from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.about_us, name='about_us'),
    url(r'^community-and-charity-involvement/$', views.get_community_and_charity, name='community-and-charity-involvement'),
    url(r'^our-people/$', views.get_our_people, name='our-people'),
    url(r'^culture-diversity/$', views.get_culture-diversity, name='culture-diversity'),
    url(r'^kids-zone/$', views.get_kids_zone, name='kids-zone'),
    url(r'^metro-bank-team/$', views.get_metro_bank_team, name='metro-bank-team'),
    url(r'^awards/$', views.get_awards, name='awards' ),
    url(r'^events/$', views.get_events, name='events')
]