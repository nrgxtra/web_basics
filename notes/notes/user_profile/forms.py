from django import forms

from notes.user_profile.models import Profile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

