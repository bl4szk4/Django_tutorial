from django.urls import path

from api import views

urlpatterns = [
    path('', views.get_routes, name='routes'),
    path('projects/', views.get_projects),
    path('projects/<str:pk>/', views.get_project),
]