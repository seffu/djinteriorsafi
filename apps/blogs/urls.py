from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='blogs'),
    path('<int:id>', views.blog, name='blog'),
    path('search', views.search, name='search'),
]
