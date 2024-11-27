from django.urls import path
from task_manager.armaturesklas import views

app_name = 'armaturesklas'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.ArmatureKlasRegistrate.as_view(), name='create'),
    path('<int:pk>/update/', views.ArmatureKlasUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.ArmatureKlasDelete.as_view(), name='delete'),
]
