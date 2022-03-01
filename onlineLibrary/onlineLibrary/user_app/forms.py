from django import forms

from onlineLibrary.user_app.models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteUser(UserForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'



