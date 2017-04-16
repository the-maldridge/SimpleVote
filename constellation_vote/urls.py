from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^view/list$', views.view_list, name='view_list'),

    url(r'^manage/poll$', views.manage_poll.as_view(),
        name="manage_poll"),
    url(r'^manage/poll/(?P<poll_id>\d+)$',
        views.manage_poll.as_view(),
        name="manage_poll"),

    url(r'^view/ballot$', views.ballot_view.as_view(),
        name="view_ballot"),
    url(r'^view/ballot/(?P<poll_id>\d+)$', views.ballot_view.as_view(),
        name="view_ballot"),
    url(r'^view/poll/(?P<poll_id>\d+)/results$', views.view_poll_results,
        name="view_poll_results"),
    url(r'^view/dashboard$', views.view_dashboard,
        name="view_dashboard"),
]
