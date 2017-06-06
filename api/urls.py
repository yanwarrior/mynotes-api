from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^notes/$', views.NoteList.as_view(), name='note-list'),
    url(r'^notes/(?P<pk>[0-9]+)/$', views.NoteDetail.as_view(), name='note-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<username>.+)/$', views.UserDetail.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)