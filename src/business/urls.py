from django.conf.urls import url
from . import views


urlpattern = [
    url(r'^$', views.business, name='bussiness'),
    url(r'^current-accounts/products/business-bank-account/$', views.get_bussiness_bank_account, name='bussiness_bank_account'),
    url(r'^current-accounts/products/commercial-current-account/$', views.get_commercial-current-account, name='commercial_current_account'),
    url(r'^current-accounts/products/community-current-account/$', views.get_community-current-account, name='community-current-account'), 
    url(r'^current-accounts/products/foreign-currency/$', views.get_foreign-currency, name='foreign-currency'), 

    url(r'^current-accounts/products/insolvency-practitioner-account/$', views.get_insolvency-practitioner-account, name='insolvency-practitioner-account'),
    url(r'^current-accounts/needsbased/switching-my-account/$', views.get_switching_my_account, name='switching_my_account'),

    url(r'^current-accounts/needsbased/switching-my-account/$', views.get_switching_my_account, name='switching_my_account'),
    url(r'^current-accounts/needsbased/what-you-need-to-open-a-business-account/$', views.get_what_you_need_to_open_a_business_account, name='what_you_need_to_open_a_business_account'),

    url(r'^current-accounts/needsbased/xero-accounting-software/$', views.get_xero-accounting-software, name='xero-accounting-software'),
    url(r'^current-accounts/needsbased/acceptcards/$', views.get_acceptcards, name='acceptcards'),

    url(r'^current-accounts/needsbased/business-service-quality/$', views.get_business-service-quality, name='business-service-quality'),
    url(r'^current-accounts/needsbased/information-about-our-business-current-account-services/$', views.get_information-about-our-business-current-account-services, name='information-about-our-business-current-account-services'),

    url(r'^current-accounts/needsbased/forum-of-private-business/$', views.get_forum-of-private-business, name='forum-of-private-business'),

    url(r'^deposits/$', views.get_business_deposits, name='business_deposits'),
    url(r'^deposits/products/business-instant-access-deposit-account/$', views.get_business-instant-access-deposit-account, name='business-instant-access-deposit-account'),
    
    url(r'^deposits/products/flexible-client-term-deposit-account/$', views.get_flexible-client-term-deposit-account, name='flexible-client-term-deposit-account'),
    url(r'^deposits/products/client-premium-deposit-account/$', views.get_client_premium_deposit_account, name='client_premium_deposit_account'),

    url(r'^deposits/products/flexible-client-term-deposit-account/$', views.get_flexible-client-term-deposit-account, name='flexible-client-term-deposit-account'),
    url(r'^deposits/products/business-notice-account/$', views.get_business-notice-account, name='business-notice-account'),
    url(r'^deposits/i-need-info-on-deposits/what-i-need-to-open-a-business-account/$', views.get_info_on_deposits, name='get_info_on_deposits'),
]