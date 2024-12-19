from django.urls import path
from task_manager.transitions import views

app_name = 'transitions'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.TransitionRegistrate.as_view(), name='create'),
    path('<int:pk>/update/', views.TransitionUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.TransitionDelete.as_view(), name='delete'),
    path('<int:pk>/', views.DetailTransition.as_view(), name='detail')
]
