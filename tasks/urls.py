from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'), 
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'), 
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'), 
    path('tasks/<int:pk>/edit/', views.task_edit, name='task_edit'), 
    path('tasks/<int:pk>/complete/', views.complete_task, name='complete_task'),
    path('tasks/<int:pk>/delete/', views.delete_task, name='task_delete'),
    path('api/', include(router.urls))
]

