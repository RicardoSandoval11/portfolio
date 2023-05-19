from django import forms
#
from captcha.fields import CaptchaField

class ContactForm(forms.Form):

    message = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'label': 'Message',
                'class': 'text-field',
                'placeholder': 'Your message here...'
            }
        )
    )

    contact = forms.CharField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'label': 'Message',
                'class': 'text-field',
                'placeholder': 'Email to contact you'
            }
        )
    )

    captcha = CaptchaField()