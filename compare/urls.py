from django.conf.urls import url
from compare import views


app_name = 'compare'

urlpatterns = [
    url(r'^$', views.compare, name='compare'),
]
