from django.urls import path
from . import views
app_name = 'logipro'
urlpatterns = [
    path('',views.login, name="login"),
    path('logipro/', views.login_required, name='logipro'),
    path('details/',views.logipro_appView,name="details"),
] 