from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog_read$', views.blog_read, name='blog_read'),
    url(r'^blog_read_view/(?P<page>[0-9]{1,3})$', views.blog_read_view, name='blog_read_view'),

    url(r'^happy$', views.happy, name='happy'),
    url(r'^save$', views.happy_save, name='happy_save'),
    url(r'^delete', views.happy_delete, name='happy_delete'),

]
