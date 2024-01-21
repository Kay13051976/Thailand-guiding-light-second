from django.shortcuts import render,redirect
from django.views import generic
from .models import Post
from .models import Popular
from .forms import AccountForm



def login(request):
    return render(request, 'home_app/login.html', {})



def index(request):
    places = Popular.objects.all()
    return render(request, 'home_app/index.html', {})





def account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST, request.FILES)
        if form.is_valid():
            return redirect('success_page') 
    else:
        form = AccountForm()

    return render(request, 'home_app/account.html', {'form': form})

def popular(request):
    places = Popular.objects.all()
    return render(request, 'home_app/popular.html', {'places': places})