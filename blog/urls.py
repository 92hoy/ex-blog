from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog_read$', views.blog_read, name='blog_read'),
] 
