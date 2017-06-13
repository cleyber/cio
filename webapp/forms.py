from django import forms

class SignIn(forms.Form):
    name = forms.Charfield(label="Nombre", required="True")
    password = models.CharField(_('Contraseña'), max_length=128, required="True")
    confirm = models.CharField(_('Confirmar contraseña'), max_length=128, required="True")
