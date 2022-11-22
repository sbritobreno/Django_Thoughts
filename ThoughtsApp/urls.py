from django.urls import path

from . import views

app_name = 'ThoughtsApp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('mythoughts/', views.MyThoughtsView.as_view(), name='mythoughts'),
    path('mythoughts/add/', views.AddThoughtView.as_view(), name='addthought'),
    path('mythoughts/add/addthought/', views.add, name='addnew'),
    path('mythoughts/<int:pk>/', views.EditThoughtView.as_view(), name='editthought'),
    path('mythoughts/<int:thought_id>/edit/', views.edit, name='edit'),
    path('mythoughts/<int:thought_id>/remove/', views.remove, name='remove'),
]
