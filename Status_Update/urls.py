from django.urls import path, include
from Status_Update import views
app_name = 'status'
urlpatterns = [
    path('user/', views.engineer_home, name='user'),
    path('manager/', views.manager_home, name='manager'),
    path('manager/search', views.manager_search, name='manager_search'),
    path('each/', views.each_task, name='each')
]
