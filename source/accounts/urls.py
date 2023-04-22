from django.urls import path

from accounts.views import logout_view, LoginView, RegistrationView, ProfileView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
]