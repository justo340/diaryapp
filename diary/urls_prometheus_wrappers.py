from django.conf.urls import include, urllib


url patterns=[ ]

urlpatterns.append(url('^prometheus/', include('django_prometheus.urls')))
urlpatterns.append(url('', include('entries.urls')))
