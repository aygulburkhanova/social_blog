from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import path
from django.urls import path, reverse_lazy  
from django.views.generic import TemplateView  
from accounts.views import RegisterView, ProfileView, follow_user, ProfileUpdateView, SettingsView, UserUpdateView

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(
            template_name='accounts/login.html',
            next_page='index'
        ),
        name='login'
    ),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('settings/', SettingsView.as_view(), name='settings'),

    path('user/<int:pk>/update', UserUpdateView.as_view(), name='user_update'),

    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/update', ProfileUpdateView.as_view(), name='profile_update'),
    
    path('password-change', PasswordChangeView.as_view(
        template_name="accounts/form.html", 
        success_url = reverse_lazy("index")), 
        name='password_change'),
        
    path('follow/<int:user_id>', follow_user, name='follow'),


]
