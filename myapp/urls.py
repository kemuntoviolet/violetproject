from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.user_categories_and_tasks, name='home'),  # Use the correct view
    path('signup/', views.signup, name='signup'),
    path('todaystasks/', views.today_tasks, name='todaystasks'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('logout/', views.logout_view, name='logout_view'),
    path('create_task/', views.create_task, name='create_task'),
    path('add_task_to_category/', views.add_task_to_category, name='add_task_to_category'),
    path('task/delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('task/complete/<int:task_id>/', views.mark_complete, name='mark_complete'),
    path('tasks/scheduled/', views.fetch_tasks_by_date, name='fetch_tasks_by_date'),


    
]

