from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from tech.models import UserProfile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    password1 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password', 'style': 'width: 300px;'}))
    password2 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password', 'style': 'width: 300px;'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'last_login', 'is_superuser', 'is_staff',
                  'is_active', 'date_joined')


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100,
                                   widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=100,
                                    widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=100,
                                    widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic', 'bio', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url')
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
            'pinterest_url': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EditProfilePageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic', 'bio', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url')
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
            'pinterest_url': forms.TextInput(attrs={'class': 'form-control'}),
        }
