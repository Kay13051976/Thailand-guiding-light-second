from django.contrib import admin
from .models import Post, Gallery, FriendRequest, Profile


@admin.register(Profile)
class  ProfileAdmin(admin.ModelAdmin):
 
    list_display = ('user', 'id_user', 'cover_image', 'country')
    search_fields = ('user', 'id_user')

class GalleryAdminTab(admin.TabularInline):
    model = Gallery


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    inlines = [GalleryAdminTab]
    list_display = ('user', 'title', 'slug', 'status', 'created_on', 'views', 'visibility', 'id_post')
    search_fields = ['title', 'content', 'id_post']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_editable = ['active']
    list_display = ['post', 'active']


@admin.register(FriendRequest)
class FriendRequestAdmin(admin.ModelAdmin):
    list_editable = ['status']
    list_display = ['user', 'friend', 'status' ]


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ['user', 'friend']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'comment', 'active']