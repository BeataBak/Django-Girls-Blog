from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name = 'home'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^my-posts/$', views.list_user_posts, name='list_user_posts'),
]