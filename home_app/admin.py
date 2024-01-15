from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    inlines = [GalleryAdminTab]
    list_display = ('title', 'slug', 'status', 'created_on', 'views', 'id_post')
    search_fields = ['title', 'content', 'id_post']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    