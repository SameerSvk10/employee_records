from . import views

from django.urls import include, path, re_path

urlpatterns = [
    re_path('^employees/$', views.get_employees),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
