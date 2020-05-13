from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('id', 'content', 'rank',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('id', 'content',)