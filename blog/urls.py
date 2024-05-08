from DRF import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from rest_framework.authtoken import views as token_view
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path("blog", views.hello_world),
    path("blog/cbv", views.Helloworld.as_view()),
    path("crypto", views.get_crypto.as_view()),
    path("user", views.get_user.as_view()),
    path("article", views.ArticleListView.as_view()),
    path("article/<int:pk>", views.ArticleDetailView.as_view()),
    path("article/add", views.ArticleAddView.as_view()),
    path("article/update/<int:pk>", views.ArticleUpdateView.as_view()),
    path("check", views.CheckToken.as_view()),
    path("login1",  token_view.obtain_auth_token),
    path("article/comments/<int:pk>", views.ArticleCommentView.as_view()),
    path("users", views.UsereDetailView.as_view()),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),

]

"""router = DefaultRouter()
router.register(r'article/viewset', views.ArticleViewSet, basename='articles')
urlpatterns += router.urls"""
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)