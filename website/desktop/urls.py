from django.conf.urls import url
# from django.conf.urls.static import static
# from django.conf import settings

from . import views

app_name = "desktop"
urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
] 
