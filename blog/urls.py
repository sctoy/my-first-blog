from django.conf.urls import url
from . import views

# ^ represents start or root URL. $ represents end.
# These two together represent and emptry string or the root URL. Homepage.
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
