from django import forms
from .models import Post, Comment

class PostModelForm(forms.ModelForm):
	content = forms.CharField(widget=forms.Textarea(attrs={'rows':4}), label='')
	class Meta:
		model = Post
		fields = ('content', 'image')

class CommentModelForm(forms.ModelForm):
	body = forms.CharField(max_length=1000, label='', widget=forms.Textarea(attrs={'placeholder':'Напишите ваш комментарий...', 'rows':3, 'cols':15}))
	class Meta:
		model = Comment
		fields = ('body',)