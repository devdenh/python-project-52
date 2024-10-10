from django.urls import path
from task_manager.links.cfs import views

app_name = 'cfs'

urlpatterns = [
    path('', views.CFSView.as_view(), name='index'),
    path('create/', views.CFSRegistrate.as_view(), name='create'),
    path('<int:pk>/update/', views.CFSUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.CFSDelete.as_view(), name='delete'),
]
