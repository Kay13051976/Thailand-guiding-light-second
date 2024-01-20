from django.shortcuts import render
from django.views import generic
from .models import Post
from .models import Popular

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = 'index.html'

    def popular(request):
        places = Popular.objects.all()
        return render(request, 'home_app/popular.html', {'places': places})