# -*- encoding: utf-8 -*-
"""
Este fichero forms.py ha sido creado con
la finalidad de validar los datos que el
usuario introduce en el formulario de registro.
Si hay algun fallo impide que 
el usuario pueda seguir con el registro.
"""
from users.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _
class RegistrationForm(forms.Form):
    #""" Clase que almacena los metodos que se
#	encargan de la validacion de los datos
 #   del formulario de registro."""
    required_css_class = 'required'
    username = forms.RegexField(regex=r'^[\w.@+-]+$', max_length=30, label=_("Username"),  widget=forms.TextInput(attrs={'placeholder': 'username', 'class':"form-control"}), error_messages={'invalid': _("Use solo letras.")})
    email = forms.CharField(label=_("E-mail"),  widget=forms.EmailInput(attrs={'placeholder': 'Insert your email', 'class':"form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password', 'class':"form-control"}), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password', 'class':"form-control"}), label=_("Password (again)"))
    def clean_username(self):
        # Valida el nombre de usuario """
        existing = User.objects.filter(username__iexact=self.cleaned_data['username'])
        if existing.exists():
            raise forms.ValidationError(_("Ya existe ese nombre de ususario."))
        else:
            return self.cleaned_data['username']

    def clean(self):
  #      """ Valida las contraseñas """
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise forms.ValidationError(_("Las contraseñas deben coincidir."))
        return self.cleaned_data
    def clean_email(self):
   #     """ Valida el e-mail """
        existing = User.objects.filter(email__iexact=self.cleaned_data['email'])
        if existing.exists():
            raise forms.ValidationError(_("Ya hay un usuario  registrado con este e-mail."))
        else:
            return self.cleaned_data['email']

