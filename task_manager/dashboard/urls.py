from django.urls import path
from task_manager.dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='index'),
    # path('create/', views.TaskRegistrate.as_view(), name='create'),
    # path('<int:pk>/update/', views.TaskUpdate.as_view(), name='update'),
    # path('<int:pk>/delete/', views.TaskDelete.as_view(), name='delete'),
    # path('<int:pk>/', views.DetailTask.as_view(), name='detail')
]
