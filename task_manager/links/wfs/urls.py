from django.urls import path
from task_manager.links.wfs import views

app_name = 'wfs'

urlpatterns = [
    path('', views.WFSView.as_view(), name='index'),
    path('create/', views.WFSRegistrate.as_view(), name='create'),
    path('<int:pk>/update/', views.WFSUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.WFSDelete.as_view(), name='delete'),
]
