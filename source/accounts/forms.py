from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Username')
    password = forms.CharField(required=True, label='Password', widget=forms.PasswordInput)


class CustomUserCreationForm(forms.ModelForm):
    username = forms.CharField(label='username')
    password = forms.CharField(required=True, label='Password', strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(required=True, label='Password_confirm', strip=False,
                                       widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'password_confirm', 'email', 'first_name', 'last_name')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пороли не совпадают!')