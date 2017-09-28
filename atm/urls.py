from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^withdraw/(?P<account_no>\d{11})/$', views.withdraw, name='withdraw'),
]
