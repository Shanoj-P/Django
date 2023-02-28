from django.urls import path
from . import views
urlpatterns = [

    path('', views.home, name='home'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update.html/<int:id1>/', views.update, name='update'),
    path('cbvhome/', views.listView.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.taskDetail.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.taskUpdate.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.taskDelete.as_view(), name='cbvdelete')
]