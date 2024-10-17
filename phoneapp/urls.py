from django.urls import path
from . import views

urlpatterns = [
    path('', views.makes, name='makes'),
    path('delete/<int:id>/', views.delete_make_view, name='delete_make'), 
    path('search/', views.search_results, name='search_results'),
    path('make_detail/<int:make_id>/', views.make_detail, name='make_detail'),
    path('makes/new/', views.new_make, name='new_make'),
]
