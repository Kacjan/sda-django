from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Profile
from django.db.transaction import atomic


class UserCreationFormCustom(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name']

    biography = forms.CharField(
        label='Tell us your story with movies', widget=forms.Textarea, min_length=5
    )

    @atomic
    def save(self, commit=True):
        result = super().save(commit)

        biography = self.cleaned_data['biography']
        profile = Profile(biography=biography, user=result)
        if commit:
            profile.save()
        return result