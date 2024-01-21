from . import views
from django.urls import path
from .views import popular,index,account


urlpatterns = [
    path('account/', account, name='account'),
    path('index/', index, name='index'),
    path('popular/', popular, name='popular'),
]