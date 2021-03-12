from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('profile/', views.profile, name='profile'),

    # sign up & activate urls
    path('signup/', views.signup, name='signup'),
    path('activation_sent/', views.activation_sent, name='activation_sent'),
    path('activation_success/', views.activation_success, name='activation_success'),
    path('activate/<uidb64>/<token>/',
        views.activate, name='activate'),

    # login / logout urls
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # change password urls
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # restore password urls
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
