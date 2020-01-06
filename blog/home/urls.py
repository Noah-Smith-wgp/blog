from django.conf.urls import url
from home.views import IndexView, DetailView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^detail/', DetailView.as_view(), name='detail'),
]
