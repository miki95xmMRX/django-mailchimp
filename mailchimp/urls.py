from django.urls import (
    re_path,
)

from .settings import VIEWS_INFO, VIEWS_OVERVIEW, VIEWS_SCHEDULE_OBJECT, VIEWS_TEST_OBJECT
from .views import webhook, dequeue, cancel, test_real


urlpatterns = [
    re_path(r'^$', VIEWS_OVERVIEW, name='mailchimp_overview', kwargs={
        'page':'1'}),
    re_path(r'^(?P<page>\d+)/$', VIEWS_OVERVIEW, name='mailchimp_overview'),
    re_path(r'^send/(?P<content_type>\d+)/(?P<pk>\d+)/$', VIEWS_SCHEDULE_OBJECT, name='mailchimp_schedule_for_object'),
    re_path(r'^test/(?P<content_type>\d+)/(?P<pk>\d+)/$', VIEWS_TEST_OBJECT, name='mailchimp_test_for_object'),
    re_path(r'^test/(?P<content_type>\d+)/(?P<pk>\d+)/real/$', test_real, name='mailchimp_real_test_for_object'),
    re_path(r'^info/(?P<campaign_id>\w+)/$', VIEWS_INFO, name='mailchimp_campaign_info'),
    re_path(r'^dequeue/(?P<id>\d+)/', dequeue, name='mailchimp_dequeue'),
    re_path(r'^cancel/(?P<id>\d+)/', cancel, name='mailchimp_cancel'),
    re_path(r'^webhook/(?P<key>\w+)/', webhook, name='mailchimp_webhook'),
]
