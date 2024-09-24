from django.urls import path
from task_manager.concrete import views

app_name = 'concrete'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.ConcreteRegistrate.as_view(), name='create'),
    path('<int:pk>/update/', views.ConcreteUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.ConcreteDelete.as_view(), name='delete'),
]
