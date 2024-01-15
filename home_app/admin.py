from django.contrib import admin
from .models import Post, Gallery



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