from django.conf.urls import url
from authentication.views import RegistrationAPIView, LoginAPIView

urlpatterns = [
    # regex url pattern that applies to API
    # 'r' for regex
    # '^' starts the URL
    # '$' denotes end of URL
    # name ensures every URL is unique
    url(r'^users/register/$', RegistrationAPIView.as_view(), name='register'),
    url(r'^users/login/$', LoginAPIView.as_view(), name='login')
]

