from django.forms import ModelForm
from .models import ContactModel
from django import forms


class ContactForm(ModelForm):
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = ContactModel
        fields = ('name', 'email', 'topic', 'message')

    def __init__(self, *args, **kwargs):                #place holders

        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'placeholder': 'Insert your name here'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Insert your email here'
        })
        self.fields['topic'].widget.attrs.update({
            'placeholder': 'Insert your topic here'
        })
        self.fields['message'].widget.attrs.update({
            'placeholder': 'Type your message here'
        })
