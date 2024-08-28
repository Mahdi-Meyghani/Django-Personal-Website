from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=500)
    email = forms.EmailField()
    message = forms.CharField(max_length=5000)