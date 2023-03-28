from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView, CreateView
from tech.models import UserProfile
from users.forms import SignUpForm, EditProfileForm, PasswordChangingForm, EditProfilePageForm, ProfilePageForm


class ProfilePage(DetailView):
    model = UserProfile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        # users = UserProfile.objects.all()
        context = super(ProfilePage, self).get_context_data(**kwargs)
        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context


class PasswordChange(PasswordChangeView):
    form_class = PasswordChangingForm
    # form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')
    # success_url = reverse_lazy('index')


def password_success(request):
    return render(request, 'registration/password_success.html', {})


class UserRegister(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEdit(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user


class CreateUserProfile(CreateView):
    model = UserProfile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile.html'
    # fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePage(generic.UpdateView):
    model = UserProfile
    form_class = EditProfilePageForm
    template_name = 'registration/edit_profile_page.html'
    # fields = ['bio', 'profile_pic', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url']
    success_url = reverse_lazy('index')
