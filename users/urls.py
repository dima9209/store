from django.urls import path
from users.views import login, logout, UserRegistrationView, UserProfileView

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', UserRegistrationView.as_view(), name='register'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('logout/', logout, name='logout')
]