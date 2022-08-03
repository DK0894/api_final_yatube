from django.urls import include, path
from rest_framework.routers import DefaultRouter


from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet


app_name = 'api'

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register(
    r'^posts/(?P<post_id>\d+)$', PostViewSet, basename='post')
router.register('groups', GroupViewSet, basename='groups')
router.register(
    r'^groups/(?P<group_id>\d+)$', GroupViewSet, basename='group')
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')
router.register(
    r'posts/(?P<post_id>\d+)/comments/(?P<comment_id>\d+)',
    CommentViewSet, basename='comment')
router.register('follow', FollowViewSet, basename='follow')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
