from django.contrib import admin
from django.urls import path

from .views import (
    home,
    room,
    createRoom,
    updateRoom,
    deleteRoom,
    loginPage,
    logoutUser,
    registerPage,
    deleteMessage,
    userProfile,
    updateUser,
    topicsPage,
    activityPage,
)

from django.contrib.auth import views as auth_views


urlpatterns = [
    path("login/", loginPage, name="login"),
    path("logout/", logoutUser, name="logout"),
    path("register/", registerPage, name="register"),
    path("", home, name="home"),
    path("room/<str:pk>/", room, name="room"),
    path("profile/<str:pk>/", userProfile, name="user-profile"),
    path("create-room/", createRoom, name="create-room"),
    path("update-room/<str:pk>/", updateRoom, name="update-room"),
    path("delete-room/<str:pk>/", deleteRoom, name="delete-room"),
    path("delete-message/<str:pk>/", deleteMessage, name="delete-message"),
    path("update-user/", updateUser, name="update-user"),
    path("topics/", topicsPage, name="topics"),
    path("activity/", activityPage, name="activity"),
    # ...
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            html_email_template_name="registration/password_reset_email.html"
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    # ...
]
