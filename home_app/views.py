from django.shortcuts import render,redirect
from django.views import generic
from .models import Post
from .models import Popular,Profile,Gallery
from .forms import AccountForm,UserPostForm



def login(request):
    return render(request, 'home_app/login.html', {})



def index(request):
    if request.method == 'POST':
        form = UserPostForm(request.POST)
        if form.is_valid():
            post_instance = form.save(commit=False)
            post_instance.user = request.user
            post_instance.save()

    
            images = request.FILES.getlist('images')
            for image in images:
                Gallery.objects.create(post=post_instance, image=image)

            
    else:
        form = UserPostForm()


    posts = Post.objects.all() #filter(user=request.user)
    return render(request, 'home_app/index.html', {
        'posts' : posts
    })





def account(request):
    if request.method == 'POST':
        print(request.POST)
        form = AccountForm(request.POST, request.FILES)
        if form.is_valid():
            profile = Profile.objects.get(user=request.user)
            if form.cleaned_data['profileimage'] != None:
                profile.profile_img = form.cleaned_data['profileimage']
            profile.phone = form.cleaned_data['phone']
            profile.save()
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.save()
            return render(request, 'home_app/your_account.html', {'form': form})
    else:
        form = AccountForm()
        user = request.user
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            profile = Profile.objects.create(user=request.user,id_user=request.user.id)
        form.fields['profileimage'].initial = profile.profile_img
        form.fields['phone'].initial = profile.phone
        form.fields['accountname'].initial = user.username
        form.fields['first_name'].initial = user.first_name
        form.fields['last_name'].initial = user.last_name
        form.fields['email'].initial = user.email
        

    return render(request, 'home_app/your_account.html', {'form': form})

def popular(request):
    places = Popular.objects.all()
    return render(request, 'home_app/most_popular_place.html', {'places': places})
