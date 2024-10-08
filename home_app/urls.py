from . import views
from django.urls import path
from .views import popular, index, account, api_toggle_like, api_add_comment, api_edit_comment, api_delete_comment, api_toggle_connect, friend_request_list, api_toggle_share, api_delete_post, api_reply_comment, about, contact


urlpatterns = [
    path('account/', account, name='account'),
    path('', index, name='index'),
    path(
        'popular/', popular, name='popular'),
    path(
        'api/toggle-like/<uuid:id_post>/',
        api_toggle_like, name='toggle-like'),
    path(
        'api/add_comment/<str:post_id>/', api_add_comment, name='add_comment'),
    path(
        'api/edit_comment/<str:comment_id>/',
        api_edit_comment, name='edit_comment'),
    path(
        'api/delete_comment/<str:comment_id>/',
        api_delete_comment, name='delete_comment'),
    path(
        'api/toggle-connect/<str:user_id>/',
        api_toggle_connect, name='friend_request'),
    path(
        'api/toggle-share/<str:post_id>/',
        api_toggle_share, name='post_share'),
    path(
        'api/delete_post/<str:post_id>/',
        api_delete_post, name='delete_comment'),
    path(
        'api/reply_comment/<str:comment_id>/',
        api_reply_comment, name='add_comment'),
    path('connection/', friend_request_list, name='connection'),
    path('comment_crud/', views.CommentsCrud, name='comment-crud'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact')

]
