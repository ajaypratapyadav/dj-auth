from django.urls import path
from accounts import views as account_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', account_view.signup, name='signup'),
    path('login/', account_view.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
