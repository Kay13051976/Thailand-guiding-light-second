from django.shortcuts import render, redirect
from django.views import generic
from .models import Post
from .models import Popular, Profile, Gallery, Comment
from .forms import AccountForm, UserPostForm,CommentsForm,CommentsFormEdit
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib import messages

# def login(request):
#     return render(request, 'home_app/login.html', {})


# def first_page(request):
#     print(request.user, request.user.is_authenticated)
#     if request.user.is_authenticated == True:
#         return redirect('/index')
#     else:
#         return redirect('/login')


def index(request):
    if request.method == 'GET':
        if 'delete_id' in request.GET:
            delete_comment = Comment.objects.get(id_post_comment=request.GET['delete_id'])
            delete_comment.delete()

    elif request.method == 'POST':
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

    posts = Post.get_list_approve()
    return render(request, 'home_app/index.html', {
        'posts': posts
    })


def account(request):
    if request.method == 'POST':
        print(request.POST)
        form = AccountForm(request.POST, request.FILES)
        if form.is_valid():
            profile = Profile.objects.get(user=request.user)
            if form.cleaned_data['profileimage'] is not None:
                profile.profile_img = form.cleaned_data['profileimage']
            profile.phone = form.cleaned_data['phone']
            profile.save()
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.save()
            return render(request, 'home_app/your_account.html', {
                'form': form})

    else:
        form = AccountForm()
        user = request.user
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            profile = Profile.objects.create(
                user=request.user, id_user=request.user.id)
        form.fields['profileimage'].initial = profile.profile_img
        form.fields['phone'].initial = profile.phone
        form.fields['accountname'].initial = user.username
        form.fields['first_name'].initial = user.first_name
        form.fields['last_name'].initial = user.last_name
        form.fields['email'].initial = user.email
    return render(request, 'home_app/your_account.html', {'form': form})


def popular(request):
    places = Popular.objects.all()
    return render(
        request, 'home_app/most_popular_place.html', {'places': places})


def api_toggle_like(request, id_post):
    post = get_object_or_404(Post, id_post=id_post)
    user = request.user

    if user in post.get_users_liked():
        post.remove_user_liked(user)
        liked = False
    else:
        post.add_user_liked(user)
        liked = True

    return JsonResponse({'liked': liked, 'like_count': post.get_count_liked()})


def api_add_comment(request, post_id):
    if request.method == 'POST':
        user = request.user
        post = get_object_or_404(Post, id_post=post_id)
        comment_text = request.POST.get('comment', '')

        if comment_text:
            comment = Comment(user=user, post=post, comment=comment_text)
            comment.save()

            # Send comment back
            comment_data = {
                'user': comment.user.username,
                'comment': comment.comment,
                'date': comment.get_date_string()
            }

            return JsonResponse({
                'success': True, 'message': 'Comment added successfully.',
                'comment': comment_data,
                'comment_count': post.comment_set.count()})
        else:
            return JsonResponse({
                'success': False, 'message': 'Comment text is required.'})

    return JsonResponse({
        'success': False, 'message': 'Invalid request method.'})


def CommentsCrud(request):
    
    if request.method == 'GET':
        if 'delete_id' in request.GET:
            delete_comment = Comment.objects.get(id_post_comment=request.GET['delete_id'])
            delete_comment.delete()
            messages.success(request, 'Comment deleted successfully!')
            return redirect('comment-crud')
    elif request.method == 'POST':
        if 'comment_edit_id' in request.POST:
            edit_comment = Comment.objects.get(id_post_comment=request.POST['comment_edit_id'])
            form = CommentsFormEdit(request.POST,instance=edit_comment)
            if form.is_valid():
                #form = form.save(commit=False)  # change is here
                #form.user = request.user  # change is here
                form.save()
                messages.success(request, 'Comment save successfully!')
                return redirect('comment-crud')
        else:
            form = CommentsForm(request.POST)
            if form.is_valid():
                #form = form.save(commit=False)  # change is here
                #form.user = request.user  # change is here
                form.save()
                messages.success(request, 'Comment save successfully!')
                return redirect('comment-crud')
    
    form = CommentsForm()
    formedit = CommentsFormEdit()
    comments = Comment.objects.all()
    context = {
    'form': form,
    'formedit':formedit,
    'commnets': comments,
    }
    return render(request, 'home_app/comment_crud.html', context)


