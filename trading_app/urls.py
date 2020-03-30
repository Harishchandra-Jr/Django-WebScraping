from django.conf.urls import url
from . import views


# TEMLPALTE TAGGING
app_name = 'trading_app'   
#app_name name is used for url injection check the index.html, line no 8, app_name should match "{% url 'trading_app:trading' %}"

urlpatterns=[

    url('trading/',views.trading, name='trading'),   ## name is imported as they are used after app_name,check the index.html, line no 8
    url('base/', views.base, name='base'),
    url('index/', views.index, name='index'),

]