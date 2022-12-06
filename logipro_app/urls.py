from django.urls import path
from . import views

app_name = 'logipro_app'
urlpatterns = [
    path('',views.login, name="login"),
    path('basicDetails/', views.basicDetailsView, name='basicDetails'),
    path('requirements/',views.requirementsView, name='requirements')
] 
