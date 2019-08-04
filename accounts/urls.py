from django.urls import path
from . import views

urlpatterns = [
    path('inscription/', views.inscription, name="inscription"),
    path('connexion/', views.login, name="login"),
    path('deconnexion/', views.logout, name="logout"),
]
