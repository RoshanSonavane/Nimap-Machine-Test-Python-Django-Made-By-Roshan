from django.urls import path
from .views import client_list_create, client_detail, create_project_for_client, user_assigned_projects

urlpatterns = [
    path('clients/', client_list_create, name='client-list-create'),
    path('clients/<int:pk>/', client_detail, name='client-detail'),
    path('clients/<int:pk>/projects/', create_project_for_client, name='create-project-for-client'),
    path('projects/', user_assigned_projects, name='user-projects'),
]
