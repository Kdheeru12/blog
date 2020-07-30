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
    path('createpost/style1',views.template1,name='style1'),
    path('createpost/style2',views.template2,name='style2'),
    path('createpost/style3',views.template3,name='style3'),
    path('createpost/style4',views.template4,name='style4'),
    path('style1',views.style1,name='style1'),
    path('style2',views.style2,name='style2'),
    path('style3',views.style3,name='style3'),
    path('style4',views.style4,name='style4'),
    path('likes',views.likes,name='likes'),
    path('logout',views.logout,name='logout'),
    path('error',views.error,name='error'),
    path('test',views.test,name='test'),
    path('video',views.video,name='video'),
    path('myvideos',views.myvideos,name='myvideos'),
]    