from django.conf.urls import url
from . import views

app_name = 'file_sharing_app'

urlpatterns = [
    url(r'^$', views.index, name='index')
]
