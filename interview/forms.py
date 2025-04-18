
from django import forms
from .models import CharacterProfile

class CharacterProfileForm(forms.ModelForm):
    class Meta:
        model = CharacterProfile
        fields = '__all__'
        widgets = {
            'personality': forms.Textarea(attrs={'rows': 2}),
            'backstory': forms.Textarea(attrs={'rows': 2}),
        }

from django import forms

class InterviewForm(forms.Form):
    question = forms.CharField(widget=forms.Textarea, label='Ask your character:')
