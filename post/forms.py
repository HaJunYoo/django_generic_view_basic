from django import forms
from .models import Post

class PostForm(forms.ModelForm):

# 어떤 모델의 form을 만들지 ...
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
        ]