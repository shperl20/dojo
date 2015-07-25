from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /advisor_dash/
    url(r'^$', views.index, name='index'),
    # ex: /advisor_dash/12189/
    url(r'^(?P<advisor_key>[0-9]+)/$', views.detail, name='detail'),
    # ex: /advisor_dash/12189/results
    url(r'^(?P<advisor_key>[0-9]+)/results/$', views.results, name='results'),
    # ex: /advisor_dash/12189/mark/
    url(r'^(?P<advisor_key>[0-9]+)/mark/$', views.mark, name='mark'),

]
