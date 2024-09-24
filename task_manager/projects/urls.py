from django.urls import path
from task_manager.projects import views

app_name = 'projects'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.ProjectsRegistrate.as_view(), name='create'),
    path('<int:pk>/update/', views.ProjectsUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.ProjectsDelete.as_view(), name='delete'),
]
