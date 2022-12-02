from django.urls import path
from . import views
app_name = 'userauth'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/',views.sign_up, name='signup'),
    path('logout/',views.logoutUser,name='logout')
] 