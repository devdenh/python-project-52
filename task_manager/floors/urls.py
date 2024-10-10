from django.urls import path
from task_manager.floors import views

app_name = 'floors'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.FloorRegistrate.as_view(), name='create'),
    path('<int:pk>/update/', views.FloorUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.FloorDelete.as_view(), name='delete'),
]
