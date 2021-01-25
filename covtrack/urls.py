from django.conf.urls import url
from covtrack import views

urlpatterns = [
    url('^$', views.home),
    url('load-data', views.load_data),
    url('view-graphical', views.show_graphical),
    url('show-india-record', views.india_update),
    url('cov-symptoms', views.covid_sypmtoms),
    url('cov-preventions', views.covid_preventions),
]
