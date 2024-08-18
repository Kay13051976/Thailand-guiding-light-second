from . import views
from django.urls import path
from .views import popular, index, account, api_toggle_like, api_add_comment, api_edit_comment, api_delete_comment


urlpatterns = [
    path('account/', account, name='account'),
    path('', index, name='index'),
    path('popular/', popular, name='popular'),
    path('api/toggle-like/<uuid:id_post>/', api_toggle_like, name='toggle-like'),
    path('api/add_comment/<str:post_id>/', api_add_comment, name='add_comment'),
    path('api/edit_comment/<str:comment_id>/', api_edit_comment, name='edit_comment'),
    path('api/delete_comment/<str:comment_id>/', api_delete_comment, name='delete_comment'),
    path('comment_crud/', views.CommentsCrud, name='comment-crud')

]
 