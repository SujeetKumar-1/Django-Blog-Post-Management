from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('upload_csv', views.upload_csv, name='upload_csv'),
]
