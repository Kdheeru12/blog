from django.contrib import admin
from django.urls import path,include,re_path
from .import views
from django.conf.urls import url, include
from django.conf import settings



urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('query',views.homepage,name='homepage'),

    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('verification',views.verification,name='verification'),
    path('createpost',views.createpost,name='createpost'),
    path('myposts',views.myposts,name='myposts'), 
    path('post-detail',views.postdetail,name='postdetail'),
    path('<slug>/post-detail',views.postdetail,name='postdetail'),
    path('post-edit/<slug>',views.save,name='save'),
    path('<slug>/post-edit',views.editpost,name='postedit'),
    path('<user>/posts',views.othersposts,name='othersposts'),
    path('<slug>/post-delete',views.deletepost,name='deletepost'),
    path('createpost/style1',views.style1,name='style1'),
    path('logout',views.logout,name='logout'),
    path('error',views.error,name='error'),

] 