"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from task_manager import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.IndexView.as_view(), name="root"),
    path("info/", views.InfoView.as_view(), name="info"),
    path("management/", views.ManagementView.as_view(), name="management"),
    path("login/", views.UserLogin.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path("users/", include("task_manager.users.urls")),
    path("statuses/", include("task_manager.statuses.urls")),
    path("tasks/", include("task_manager.tasks.urls")),
    path("labels/", include("task_manager.labels.urls")),
    path("concrete/", include("task_manager.concrete.urls")),
    path("projects/", include("task_manager.projects.urls")),
    path("sections/", include("task_manager.sections.urls")),
    path("columns/", include("task_manager.columns.urls")),
    path("walls/", include("task_manager.walls.urls")),
    path("slabs/", include("task_manager.slabs.urls")),
    path("transitions/", include("task_manager.transitions.urls")),
    path("floors/", include("task_manager.floors.urls")),
    path("links/", include("task_manager.links.urls")),
    path("dashboard/", include("task_manager.dashboard.urls")),
]
