# -*- coding: utf-8 -*-

from django import forms

class SignIn(forms.Form):
    name = forms.CharField(label="Nombre", required="True")
    password = forms.CharField(_('Contraseña'), max_length=128, required="True")
    confirm = forms.CharField(_('Confirmar contraseña'), max_length=128, required="True")
