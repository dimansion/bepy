from django import forms
from .models import Post
from pagedown.widgets import PagedownWidget

class PostForm(forms.ModelForm):
	content = forms.CharField(widget=PagedownWidget(show_preview=False))
	published_date = forms.DateField(widget=forms.SelectDateWidget)
	class Meta:
		model = Post
		fields = [
            'title',
            'content',
            'published_date',
            'category',
        ]