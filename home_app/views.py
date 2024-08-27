from django.shortcuts import render, redirect
# from django.views import generic
from .models import Post
from django.db.models import Count
from .models import Popular, Profile, \
    Gallery, Comment, User, FriendRequest, Friend, Share
from .forms import AccountForm, UserPostForm, CommentsForm, CommentsFormEdit
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
        if 'post_edit' in request.GET:
            posts = Post.get_list_approve().filter(
                id_post=request.GET['post_edit']
            ).order_by('-created_on').annotate(
                friend_count=Count('user__Friend_user')
            )
            return render(request, 'home_app/post_edit.html',
                          {'posts': posts,
                           'post_id': request.GET['post_edit']})

        if 'photo_id' in request.GET:
            Gallery.objects.filter(post=request.GET['post_id'],
                                   image=request.GET['photo_id']).delete()
            posts = Post.get_list_approve().filter(
                id_post=request.GET['post_id']
            ).order_by('-created_on').annotate(
                friend_count=Count('user__Friend_user')
            )

            return render(request, 'home_app/post_edit.html',
                          {'posts': posts,
                           'post_id': request.GET['post_id']})

    elif request.method == 'POST':
        if 'post_id' in request.POST:
            post = get_object_or_404(Post, id_post=request.POST['post_id'])
            if 'title' in request.POST:
                post.title = request.POST['title']
                post.save()
                images = request.FILES.getlist('images')
                total_files_submitted = 0
                for file in images:
                    total_files_submitted += 1

                if total_files_submitted > 0:
                    # Gallery.objects.filter(post=post).delete()
                    for image in images:
                        Gallery.objects.create(post=post, image=image)

            posts = Post.get_list_approve().filter(
                id_post=request.POST['post_id']
            ).order_by('-created_on').annotate(
                friend_count=Count('user__Friend_user')
            )

            return render(request,
                          'home_app/post_edit.html',
                          {'posts': posts,
                           'post_id': request.POST['post_id']})

        else:
            form = UserPostForm(request.POST)
            if form.is_valid():
                post_instance = form.save(commit=False)
                post_instance.user = request.user
                post_instance.save()
                images = request.FILES.getlist('images')
                for image in images:
                    Gallery.objects.create(post=post_instance, image=image)

        posts = Post.get_list_approve().order_by('-created_on').annotate(
            friend_count=Count('user__Friend_user')
        )

    else:
        form = UserPostForm()

    if request.method == 'GET':
        if 'post_id' in request.GET:
            posts = Post.get_list_approve().filter(
                id_post=request.GET['post_id']
            ).order_by('-created_on').annotate(
                friend_count=Count('user__Friend_user')
            )
        else:
            posts = Post.get_list_approve().order_by('-created_on').annotate(
                friend_count=Count('user__Friend_user')
            )

    full_url = request.build_absolute_uri()
    return render(request, 'home_app/index.html', {
        'posts': posts,
        'full_url': full_url
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


def api_toggle_connect(request, user_id):
    if not request.user.is_authenticated:
        return redirect('login')

    user = get_object_or_404(User, id=request.user.id)
    friend = get_object_or_404(User, id=user_id)

    if str(request.user.id) ==  str(user_id):
        connected = False
    elif not FriendRequest.objects.filter(user=user, friend=friend).exists():
        if not FriendRequest.objects.filter(user=friend, friend=user).exists():
            friendRequest = FriendRequest.objects.create(
            user=user, friend=friend, status="pending"
            )
            friendRequest.save()
            connected = True
    else:
        connected = False

    return JsonResponse({'connected': connected})


def api_toggle_share(request, post_id):
    if not request.user.is_authenticated:
        return redirect('login')

    post = get_object_or_404(Post, id_post=post_id)
    user = get_object_or_404(User, id=request.user.id)

    if not Share.objects.filter(user=user, post=post).exists():
        share = Share.objects.create(
            user=user, content="Share Post", post=post
        )
        share.save()
        shared = True
    else:
        shared = False

    return JsonResponse({'shared': shared,
                         'share_count': post.shared_posts.count()})


def friend_request_list(request):
    if request.method == 'GET':
        if 'delete_request_id' in request.GET:
            delete_friend_request = FriendRequest.objects.get(
                id_friend_request=request.GET['delete_request_id']
            )
            delete_friend_request.delete()
            messages.success(request, 'Friend Request Canceled successfully!')
            return redirect('connection')

        if 'friend_request_id' in request.GET:
            friend_request_id = request.GET['friend_request_id']
            # Get the FriendRequest object
            friend_request = get_object_or_404(
                FriendRequest, id_friend_request=friend_request_id
            )

            # Ensure the request is for the current user
            if friend_request.friend is request.user:
                return redirect('connection')

            # Update the status to 'accept'
            friend_request.status = 'accept'
            friend_request.save()

            # Create a Friend relationship for both users
            Friend.objects.create(
                user=friend_request.user, friend=friend_request.friend
            )
            Friend.objects.create(
                user=friend_request.friend, friend=friend_request.user
            )

            messages.success(request, 'Friend Request Canceled successfully!')
            return redirect('connection')

        if 'friend_id' in request.GET:
            friend = get_object_or_404(User, id=request.GET['friend_id'])
            user = request.user
            Friend.unfriend(user, friend)
            FriendRequest.objects.filter(user=user, friend=friend).delete()
            FriendRequest.objects.filter(user=friend, friend=user).delete()

    friendRequest = FriendRequest.objects.filter(
        user=request.user

    )

    friendRequestReceived = FriendRequest.objects.filter(
        friend=request.user,
        status="pending"
    )

    friend = Friend.objects.filter(
        user=request.user
    )

    context = {
        'FriendRequest': friendRequest,
        'FriendRequestReceived': friendRequestReceived,
        'Friend': friend
    }
    return render(request, 'home_app/connection.html', context)


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


def api_edit_comment(request, comment_id):

    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, id_post=post_id)
        Commentt = Comment.objects.get(pk=comment_id)
        comment_text = request.POST.get('comment', '')

        if comment_text:
            Commentt.comment = comment_text
            Commentt.save()

            # Send comment back
            comment_data = {
                'user': Commentt.user.username,
                'comment': Commentt.comment,
                'date': Commentt.get_date_string()
            }

            return JsonResponse({
                'success': True, 'message': 'Comment Update successfully.',
                'comment': comment_data,
                'comment_count': post.comment_set.count()})
        else:
            return JsonResponse({
                'success': False, 'message': 'Comment text is required.'})

    return JsonResponse({
        'success': False, 'message': 'Invalid request method.'})


def api_delete_comment(request, comment_id):

    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, id_post=post_id)
        Commentt = Comment.objects.get(pk=comment_id)

        if comment_id is not None:
            Commentt.delete()

            # Send comment back
            comment_data = {
                'user': Commentt.user.username,
                'comment': Commentt.comment,
                'date': Commentt.get_date_string()
            }

            return JsonResponse({
                'success': True, 'message': 'Comment Update successfully.',
                'comment': comment_data,
                'comment_count': post.comment_set.count()})
        else:
            return JsonResponse({
                'success': False, 'message': 'Comment is required to delete.'})

    return JsonResponse({
        'success': False, 'message': 'Invalid request method.'})


def api_delete_post(request, post_id):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, id_post=post_id)

        if post_id is not None:
            post.delete()

            # Send comment back
            post_data = {
                'user': post.user.username,
                'post': post.id_post,
                'date': post.title
            }

            return JsonResponse({
                'success': True, 'message': 'Post deleted successfully.',
                'post': post_data
                })
        else:
            return JsonResponse({
                'success': False, 'message': 'Post is required to delete.'})

    return JsonResponse({
        'success': False, 'message': 'Invalid request method.'})


def api_add_comment(request, post_id):
    if request.method == 'POST':
        user = request.user
        post = get_object_or_404(Post, id_post=post_id)
        comment_text = request.POST.get('comment', '')

        if comment_text:
            comment = Comment(user=user, post=post, comment=comment_text)
            comment.save()
            # imagepath ='/media/images/default/profile.png'
            # if comment.user.profile.get_profile_url is None:
            #    imagepath = '/media/images/default/profile.png'
            # else:
            #    imagepath= comment.user.profile.get_profile_url
            # Send comment back
            comment_data = {
                'user': comment.user.username,
                'comment': comment.comment,
                'date': comment.get_date_string(),
                'id_post_comment': comment.id_post_comment
                # 'get_profile_url': imagepath
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
            delete_comment = Comment.objects.get(
                id_post_comment=request.GET['delete_id']
            )
            delete_comment.delete()
            messages.success(request, 'Comment deleted successfully!')
            return redirect('comment-crud')
    elif request.method == 'POST':
        if 'comment_edit_id' in request.POST:
            edit_comment = Comment.objects.get(
                id_post_comment=request.POST['comment_edit_id']
            )
            form = CommentsFormEdit(request.POST, instance=edit_comment)
            if form.is_valid():
                # form = form.save(commit=False)  # change is here
                # form.user = request.user  # change is here
                form.save()
                messages.success(request, 'Comment save successfully!')
                return redirect('comment-crud')
        else:
            form = CommentsForm(request.POST)
            if form.is_valid():
                # form = form.save(commit=False)  # change is here
                # form.user = request.user  # change is here
                form.save()
                messages.success(request, 'Comment save successfully!')
                return redirect('comment-crud')

    form = CommentsForm()
    formedit = CommentsFormEdit()
    comments = Comment.objects.all()
    context = {
        'form': form,
        'formedit': formedit,
        'commnets': comments,
    }
    return render(request, 'home_app/comment_crud.html', context)
