from . import views
from django.urls import path
from .views import UserRegister, UserEdit, PasswordChange, ProfilePage, EditProfilePage, CreateUserProfile

urlpatterns = [
    path('Signup/', UserRegister.as_view(), name="register"),
    path('edit_settings/', UserEdit.as_view(), name="edit_settings"),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password/', PasswordChange.as_view(template_name="registration/change-password.html")),
    path('password_success', views.password_success, name="password_success"),
    path('<int:pk>/profile/', ProfilePage.as_view(), name="profile_page"),
    path('<int:pk>/edit_profile/', EditProfilePage.as_view(), name="edit_profile_page"),
    path('create_profile_page/', CreateUserProfile.as_view(), name="create_user_profile"),
]
