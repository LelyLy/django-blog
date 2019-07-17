from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['author']}),
        (None, {'fields': ['title', 'text', 'created_date']}),
    ]
    list_display = ('author', 'title', 'created_date')
    search_fields = ['title']


admin.site.register(Post, PostAdmin)
