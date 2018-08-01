from django.conf.urls import url
from . import views

# шаблон

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]