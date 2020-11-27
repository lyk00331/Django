from django.contrib import admin
from board.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'writer', 'title', 'content', 'time', 'password')

admin.site.register(Post, PostAdmin)