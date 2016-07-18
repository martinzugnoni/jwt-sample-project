from django.conf.urls import url

from sample.views import RestrictedView


urlpatterns = [
    url(r'^restricted/$', RestrictedView.as_view()),
]
