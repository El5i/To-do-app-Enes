from django.urls import path
from .views import home, create_task, uncompleted_tasks, completed_tasks

urlpatterns = [
    path('', home, name='home'),
    path('create/', create_task, name='create_task'),
    path('uncompleted/', uncompleted_tasks, name='uncompleted_tasks'),
    path('completed/', completed_tasks, name='completed_tasks'),
]
