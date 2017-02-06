from django.conf.urls import url
from ublog import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
