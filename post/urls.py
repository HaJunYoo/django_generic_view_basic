from django.urls import include, path
from post.views import *


urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    # 링크의 id에 매핑해서 view 내의 함수에 전달해서 템플릿에 보여줌
    path("posts/<int:post_id>", PostDetailView.as_view(), name="post-detail"),
    path("posts/new/", PostCreateView.as_view(), name="post-create"),
    path("posts/<int:post_id>/edit/", PostUpdateView.as_view(), name="post-update"),
    path("posts/<int:post_id>/delete/", PostDeleteView.as_view(), name="post-delete"),
]