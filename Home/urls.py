from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="Home"),
    path('accounts/registration/', views.RegisterFormView.as_view(), name="registration"),
    path('specialty/', views.SpecialtyView.as_view(), name='specialty'),
    path('specialty/<str:slug>/', views.specialty_single_page, name="specialty"),
    path('profil/<username>/', views.profil_user, name="profil"),
]