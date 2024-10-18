from django.urls import path
from task_manager.links.tfs import views

app_name = 'tfs'

urlpatterns = [
    path('', views.TFSView.as_view(), name='index'),
    path('create/', views.TFSRegistrate.as_view(), name='create'),
    path('<int:pk>/update/', views.TFSUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.TFSDelete.as_view(), name='delete'),
]
