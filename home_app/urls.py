from . import views
from django.urls import path
from .views import popular

urlpatterns = [
    path('', views.PostList.as_view(), name='home_app')
]

urlpatterns = [
    path('popular/', popular, name='popular'),
]