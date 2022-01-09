from django.contrib import admin
from .models import Post
from django.utils.safestring import mark_safe

# Register your models here.

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message', 'message_length', 'is_public', 'created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width: 72px;" />')
        return None

        return len(post.message)

    def message_length(self, post):
        # return len(post.message)
        return f"{len(post.message)} 글자"
