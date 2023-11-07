from typing import Any
from django import forms
from clientes.models import User

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

    def save(self, commit=True):
        password = self.cleaned_data['password']
        user = super().save(commit=False)
        user.set_password(password)
        if commit:
            user.save()        
        return user
