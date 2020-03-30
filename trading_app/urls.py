from django.conf.urls import url
from . import views


# TEMLPALTE TAGGING
app_name = 'trading_app'

urlpatterns=[

    url('trading/',views.trading, name='trading'),
    url('base/', views.base, name='base'),
    url('index/', views.index, name='index'),

]