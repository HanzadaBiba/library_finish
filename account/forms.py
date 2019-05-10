from django import forms
from django.contrib.auth.models import User
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль',
    widget=forms.PasswordInput)
    password2 = forms.CharField(label='Пароль кайталау',
    widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        widgets = {
            "username": forms.TextInput(attrs={ 'label': 'Логин'}),
            "first_name": forms.TextInput(
                attrs={'label': 'Есімі'}),
            "email": forms.TextInput(
                attrs={'label': 'Почта'}),

        }
        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Парольдар сәйкес келмейді!')
            return cd['password2']
