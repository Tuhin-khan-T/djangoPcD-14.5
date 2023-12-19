from django.urls import path
from login import views

urlpatterns = [
    path('', views.loginHome, name='home'),
    path('form/', views.loginform, name='form'),
    path('djangoForms/',views.djangoForm,name="dform") 
]