from django.urls import path
from task_manager.slabs import views

app_name = 'slabs'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.SlabRegistrate.as_view(), name='create'),
    path('<int:pk>/update/', views.SlabUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.SlabDelete.as_view(), name='delete'),
]
