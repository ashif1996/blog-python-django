from django.urls import path
from .views import Home, ArticleDetail, AddPost, UpdatePost, DeletePost, AddCategory, CategoryView, LikeView, AddComment

urlpatterns = [
    path('', Home.as_view(), name="index"),
    path('article/<int:pk>', ArticleDetail.as_view(), name="article-details"),
    path('add_post/', AddPost.as_view(), name="add_post"),
    path('add_category/', AddCategory.as_view(), name="add_category"),
    path('article/edit/<int:pk>', UpdatePost.as_view(), name="update_post"),
    path('article/delete/<int:pk>', DeletePost.as_view(), name="delete_post"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('article/<int:pk>/comment/', AddComment.as_view(), name="add_comment"),
]
