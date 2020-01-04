from django.conf.urls import url
from home.views import IndexView, DetailView


urlpatterns = [
    url('', IndexView.as_view(), name='index'),
    url('detail/', DetailView.as_view(), name='detail'),
]
