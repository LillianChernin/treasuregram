from django.conf.urls import url
from .views import index
from .views import show
from .views import post_treasure
from .views import profile

urlpatterns = [
    url(r'^user/(\w+)/$', profile, name='profile'),
    url(r'^$', index),
    url(r'^([0-9]+)/$', show, name = 'show'),
    url(r'^post_url/$', post_treasure, name="post_treasure")
]
