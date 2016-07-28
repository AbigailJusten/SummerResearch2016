from django.conf.urls import url, include
from django.views.generic.list import ListView
from django.views.generic.detail import  DetailView
from jobdata.models import Jobdata
from . import views

#Already leading with whatever URL is used to get to jobdata
urlpatterns = [
	
	url(r'^$', ListView.as_view(queryset=Jobdata.objects.all().\
order_by("major")[:100]), name="jobdata - home"),
	url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Jobdata),\
	name = 'job-listing')

]
