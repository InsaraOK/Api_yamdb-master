from api.views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                       ReviewViewSet, TitleViewSet)
from django.urls import include, path
from rest_framework import routers

from .views import AdminUserViewset, get_token, signup

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register('users', AdminUserViewset, basename='users')
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('titles', TitleViewSet, basename='titles')
router_v1.register(r'titles/(?P<title_id>\d+)/reviews',
                   ReviewViewSet, basename='review')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comment')

urlpatterns = [
    path(
        'v1/auth/signup/',
        signup,
        name='user_signup'
    ),
    path(
        'v1/auth/token/',
        get_token,
        name='token_obtain'
    ),
    path('v1/', include(router_v1.urls), name='v1'),
]