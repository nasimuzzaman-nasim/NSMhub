from .models import Blog
from django import forms
from django.contrib.auth.models import User


class BlogForm(forms.ModelForm):
    # Blog.user = forms.CharField(initial='abc')

    class Meta:
        model = Blog
        fields = [
            # 'user',
            'title',
            'post'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        return title
