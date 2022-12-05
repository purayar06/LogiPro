from django.urls import path
from . import views
app_name = 'logipro'
urlpatterns = [
    path('',views.login, name="login"),
    path('basicDetails/', views.logipro_appView, name='basicDetails'),
] 