from . import views
from django.urls import path
from .views import popular, index, account, api_toggle_like, api_add_comment, first_page


urlpatterns = [
    path('', first_page, name='first_page'),
    path('account/', account, name='account'),
    path('index/', index, name='index'),
    path('popular/', popular, name='popular'),
    path(
        'api/toggle-like/<uuid:id_post>/',
        api_toggle_like, name='toggle-like'),
    path(
        'api/add_comment/<str:post_id>/', api_add_comment, name='add_comment'),
]
