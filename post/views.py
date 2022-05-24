import imp
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post
from .forms import PostForm

# post라는 모델을 정해준 템플릿에 뿌려줄 것이다.
class IndexView(ListView):
    model = Post
    template_name = "post/index.html"
    context_object_name = "posts"

# pk id에 따라서 정해진 템플릿에 뿌려줄 것이다
class PostDetailView(DetailView):
    model = Post
    template_name = "post/post_detail.html"
    context_object = "post"
    pk_url_kwarg = "post_id"

class PostCreateView(CreateView):
    model = Post
    template_name = "post/post_form.html"
    form_class = PostForm

    def get_success_url(self):
        return reverse('index')

# create랑 같은데 pk id 여부만 다름
class PostUpdateView(UpdateView):
    model = Post
    template_name = "post/post_form.html"
    form_class = PostForm
    pk_url_kwarg = "post_id"
    # post 객체의 id를 받아서 url 리턴
    def get_success_url(self):
        return reverse('post-detail', kwargs={'post_id': self.object.id})

class PostDeleteView(DeleteView):
    model = Post
    template_name = "post/post_confirm_delete.html"
    pk_url_kwarg = 'post_id'

    def get_success_url(self):
        return reverse('index')