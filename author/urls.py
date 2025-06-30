from django.urls import path
from author.views import AuthorViewSet

author_list = AuthorViewSet.as_view(actions={
    "get": "list",
    "post": "create",
})
movie_detail = AuthorViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})
urlpatterns = [
    path("authors/", author_list, name="author-list"),
    path("authors/<int:pk>", movie_detail, name="author-detail"),
]

app_name = "author"
