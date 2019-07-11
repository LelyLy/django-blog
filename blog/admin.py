from django.contrib import admin
from djangogirls.blog.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['author']}),
        (None, {'fields': ['title', 'text', 'created_date']}),
    ]
    list_display = ('author', 'title', 'created_date')
    search_fields = ['title']


admin.site.register(Post, PostAdmin)

#
# class CommentAdmin(admin.ModelAdmin):
#     fields = ['author', 'text', 'created_date']
#     list_display = ('author', 'title', 'created_date')
#     search_fields = ['title']
#
#
admin.site.register(Comment)
