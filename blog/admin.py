from django.contrib import admin
from blog.models import Category, Post

class PostAdmin(admin.ModelAdmin):
	list_filter = ["published_date"]
	list_display = ('title', 'published_date',)
	prepopulated_fields = {'slug':('title',)}
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)