from django.contrib import admin
from django.urls import path

from testapp.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index.as_view(),name='index'),
    path('post/new/',BlogCreateView.as_view(),name='post_new'),
    path('post/<int:pk>/',BlogDetailView.as_view(),name='postdetail'),
    path('post/<int:pk>/edit/',BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/',BlogDeleteView.as_view(), name='post_delete'),
    
]
