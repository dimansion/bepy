from django.contrib import admin
from blog.models import Category, Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category','published_date',)
    prepopulated_fields = {'slug':('title',)}
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
