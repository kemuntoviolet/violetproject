from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
	path('home/', views.home, name = 'home'), 	
	path('signup/', views.signup, name = 'signup'),
 	path('todaystasks/', views.todaystasks, name = 'todaystasks'),
  	path('viewalltasks/', views.viewalltasks, name = 'viewalltasks'),
   	path('about/', views.about, name = 'about'),
    path('search/', views.search, name = 'search'),
    path('logout/', views.logout_view, name = 'logout_view'),
    path('addcategory/', views.addcategory, name = 'addcategory'),
    path('create_task/', views.create_task, name = 'create_task'),

]
