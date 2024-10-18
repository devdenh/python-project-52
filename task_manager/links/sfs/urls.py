from django.urls import path
from task_manager.links.sfs import views

app_name = 'sfs'

urlpatterns = [
    path('', views.SFSView.as_view(), name='index'),
    path('create/', views.SFSRegistrate.as_view(), name='create'),
    path('<int:pk>/update/', views.SFSUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.SFSDelete.as_view(), name='delete'),
]
