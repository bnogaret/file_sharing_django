from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'file_sharing_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='sign_up'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout_then_login, name='logout'),
    url(r'^group/$', views.group, name='group')
]
