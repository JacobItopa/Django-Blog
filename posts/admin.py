from django.contrib import admin
from .models import Post, Comments, PostView, Like, User
# Register your models here.

admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(PostView)
admin.site.register(Like)
admin.site.register(User)