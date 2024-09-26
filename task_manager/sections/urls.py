from django.urls import path
from task_manager.sections import views

app_name = 'sections'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.SectionRegistrate.as_view(), name='create'),
    path('<int:pk>/update/', views.SectionUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.SectionDelete.as_view(), name='delete'),
]
