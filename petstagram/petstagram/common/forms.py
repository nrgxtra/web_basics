from django import forms

from petstagram.common.models import Comment


# class CommentForm(forms.Form):
#     comment = forms.CharField(
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'form-control rounded-2',
#             }
#         ),
#     )
from petstagram.pets.models import Pet


class CommentForm(forms.ModelForm):
    pet_pk = forms.CharField(
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Comment
        fields = ('comment', 'pet_pk')

    def save(self, commit=True):
        pet_pk = self.cleaned_data['pet_pk']
        pet = Pet.objects.get(pk=pet_pk)
        comment = Comment(
            comment=self.cleaned_data['comment'],
            pet=pet,
        )
        if commit:
            comment.save()
        return comment


