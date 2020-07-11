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
    path('post-detail',views.postdetail,name='postdetail'),
    path('<slug>/post-detail',views.postdetail,name='postdetail'),
    path('createpost/style1',views.style1,name='style1'),
    path('logout',views.logout,name='logout'),
    path('error',views.error,name='error'),

] 