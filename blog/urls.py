from django.urls import path
from . import views
from rest_framework.authtoken import views as token_view
urlpatterns = [

    path("blog", views.hello_world),
    path("blog/cbv", views.Helloworld.as_view()),
    path("crypto", views.get_crypto.as_view()),
    path("user", views.get_user.as_view()),
    path("article", views.ArticleListView.as_view()),
    path("article/<int:pk>", views.ArticleDetailView.as_view()),
    path("article/add", views.ArticleaddView.as_view()),
    path("article/update/<int:pk>", views.ArticleUpdateView.as_view()),
    path("check", views.CheckToken.as_view()),
    path("login",  token_view.obtain_auth_token),

]

