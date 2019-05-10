from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=255,verbose_name='Есімініз')
    email=models.EmailField(verbose_name='Электрондық почтаныз')
    subject=models.CharField(max_length=255,verbose_name='Хат атауы')
    text=models.CharField(verbose_name='Текст',max_length=255)
    def __str__(self):
        return self.subject
    class Meta:
        verbose_name='Письмо'
        verbose_name_plural='Письмо'
from django import forms
class Contact_form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email','subject','text')
        widgets = {
            "name": forms.TextInput(attrs={'label': 'Логин','class':'form-control','placeholder':'Есімініз'}),
            "email": forms.TextInput(attrs={'label': 'Логин','class':'form-control','placeholder':'Почта'}),
            "subject": forms.TextInput(attrs={'label': 'Логин','class':'form-control','placeholder':'Хат атауы'}),
            "text": forms.TextInput(attrs={'label': 'Логин','class':'form-control','placeholder':'Хат'}),

        }