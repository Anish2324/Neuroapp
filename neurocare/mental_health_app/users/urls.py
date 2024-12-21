from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path("exercise/", views.exercise_view, name="exercise"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("game1/", views.game1_view, name="game1"),
    path("game2/", views.game2_view, name="game2"),
    path("", views.landing_view, name="landing"),
]
