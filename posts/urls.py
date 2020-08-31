from django.contrib import admin
from django.urls import path,include,re_path
from .import views
from django.conf.urls import url, include
from django.conf import settings
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('blogs',views.blogs,name='blogs'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('verification',views.verification,name='verification'),
    path('createpost',views.createpost,name='createpost'),
    path('myposts',views.myposts,name='myposts'), 
    path('post-detail',views.postdetail,name='postdetail'),
    path('add-email',views.addemail,name='addemail'),
    path('<slug>/post-detail',views.postdetail,name='postdetail'),
    path('<slug>/edit',views.edit,name='edit'),
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
    path('tags',views.tags,name='tag'),
    path('tags/<slug>',views.tagsslug,name='tags'),
    path('serialized/<slug>',views.post_serialized_view,name='serialized'),
    path('profile',views.profile,name='profile'),
    path('profile-edit',views.profileedit,name='yourprofile'),
    path('feedback',views.feedback,name='feedback'),
    path('contact-us',views.contact,name='contact'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='reset_password.html'),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),name='password_reset_complete'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), 
        name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), 
        name='password_change'),
]    