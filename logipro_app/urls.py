from django.urls import path
from . import views
app_name = 'logipro'
urlpatterns = [
    path('', views.index, name='index'),
    path('logipro/', views.login_required, name='logipro'),
    
] 