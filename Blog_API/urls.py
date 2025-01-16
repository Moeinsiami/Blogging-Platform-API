from . import views
from django.urls import path

app_name = 'Blog_API'

urlpatterns = [
    path('', views.index, name='index'),
]
