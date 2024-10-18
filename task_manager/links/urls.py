from django.urls import path, include
from task_manager.links import views

app_name = 'links'

urlpatterns = [
    path('', views.LinksView.as_view(), name='index'),
    path('cfs/', include('task_manager.links.cfs.urls')),
    path('wfs/', include('task_manager.links.wfs.urls')),
    path('sfs/', include('task_manager.links.sfs.urls')),
    path('tfs/', include('task_manager.links.tfs.urls'))
]
