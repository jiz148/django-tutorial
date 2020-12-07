from django.urls import path

from . import views

app_name = 'hello'

urlpatterns = [
    path('', views.HelloView.as_view(), name='index'),
]
