from django.urls import path
from . import views
urlpatterns=[

path("blog",views.hello_world),
path("blog/cbv",views.Helloworld.as_view()),
path("crypto",views.get_crypto.as_view()),
path("user",views.get_user.as_view()),
path("article",views.ArticleListView.as_view()),
path("article/<int:pk>",views.ArticleDetailView.as_view()),

]

