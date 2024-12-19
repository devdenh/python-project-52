from django.urls import path
from task_manager.columns import views

app_name = 'columns'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.ColumnRegistrate.as_view(), name='create'),
    path('<int:pk>/update/', views.ColumnUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.ColumnDelete.as_view(), name='delete'),
    path('<int:pk>/', views.ColumnDetail.as_view(), name='detail')
]
