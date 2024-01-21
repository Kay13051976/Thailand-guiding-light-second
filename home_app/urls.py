from . import views
from django.urls import path
from .views import popular,index,account,login


urlpatterns = [
    path('account/', account, name='account'),
    path('index/', index, name='index'),
    path('account/', index, name='account'),
    path('login/', login, name='login'),
    path('popular/', popular, name='popular'),
]