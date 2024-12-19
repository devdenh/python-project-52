from django.urls import path
from task_manager.walls import views

app_name = 'walls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.WallRegistrate.as_view(), name='create'),
    path('<int:pk>/update/', views.WallUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.WallDelete.as_view(), name='delete'),
    path('<int:pk>/', views.WallDetail.as_view(), name='detail')
]
