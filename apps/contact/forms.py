from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'subject', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Full Name', 'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'your@email.com', 'class': 'form-input'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Message Subject', 'class': 'form-input'}),
            'message': forms.Textarea(attrs={'placeholder': 'Write your message here...', 'rows': 5, 'class': 'form-input'}),
        }

    def clean_honeypot(self):
        value = self.cleaned_data.get('honeypot', '')
        if value:
            raise forms.ValidationError('Spam detected.')
        return value
