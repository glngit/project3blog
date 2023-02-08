from django.contrib import admin
from checkapp.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display=['companey','title','slug','author','body','publish','created','updated','status','phonenumber','email','address']
    prepopulated_fields={'slug':('companey',)}
    list_filter=('status','author')
    search_fields=('title','body')
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=['status','publish']
admin.site.register(Post,PostAdmin)

from checkapp.models import Comment
class CommentAdmin(admin.ModelAdmin):
    list_display=('name','email','post','body','created','updated','active')
    list_filter=('active','created','updated')
    search_fileds=('name','email','body')
admin.site.register(Comment,CommentAdmin)
