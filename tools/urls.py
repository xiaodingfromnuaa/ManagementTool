
from django.urls import path

from tools.views import project

urlpatterns = [
    path('project/list', project.project_list, name='project_list')
]