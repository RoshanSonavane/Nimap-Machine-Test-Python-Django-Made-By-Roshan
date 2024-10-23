from django.contrib import admin
from .models import Client, Project

# Register the Client model in admin
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'client_name', 'created_by', 'created_at', 'updated_at']
    search_fields = ['client_name', 'created_by__username']
    list_filter = ['created_at']
    readonly_fields = ['created_at', 'updated_at']

# Register the Project model in admin
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'project_name', 'client', 'created_by', 'created_at']
    search_fields = ['project_name', 'client__client_name', 'created_by__username']
    list_filter = ['created_at', 'client']
    readonly_fields = ['created_at']

    # To handle Many-to-Many relationships in the admin, we can display users for each project.
    filter_horizontal = ['users']
