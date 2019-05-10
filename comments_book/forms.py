from django import forms
from comments_book.models import Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['body']
        widgets = {
            "body": forms.Textarea(attrs={'label': 'Комментария:'}),

        }
