from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-input'}),
            'body': forms.Textarea(attrs={'placeholder': 'Write your comment...', 'rows': 4, 'class': 'form-input'}),
        }
        labels = {
            'body': 'Comment',
        }
