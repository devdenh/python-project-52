from django.urls import path
from task_manager.armatures import views

app_name = 'armatures'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.ArmatureRegistrate.as_view(), name='create'),
    path('<int:pk>/update/', views.ArmatureUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.ArmatureDelete.as_view(), name='delete'),
]
