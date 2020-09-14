from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from api.views import SubjectViewSet, SubjectTopic, SingleSubjectTopic, TopicViewSet

router = routers.DefaultRouter()
router.register('subject', SubjectViewSet, basename = 'subject')
router.register('topic', TopicViewSet, basename = 'topic')

# no ^ needed bc of r
# ?P for parameter
# \d+ accepts digits between 0 and 9
custom_urlpatterns = [
    url(r'subject/(?P<subject_pk>\d+)/topic$', SubjectTopic.as_view(), name = 'subject_topic'),
    url(r'subject/(?P<subject_pk>\d+)/topic/(?P<pk>\d+)$', SingleSubjectTopic.as_view(), name = 'single_subject_topic')
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns

"""
urlpatterns = [
   path('', include(router.urls))
]
"""

