from django.contrib import admin
from project.models import Page, Content

class ContentInline(admin.TabularInline):
    model = Content
    prepopulated_fields = {'slug':('name',)}  

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date',)
    prepopulated_fields = {'slug':('title',)}
    inlines = [ContentInline]

# class ContentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'lesson',)
#     prepopulated_fields = {'slug':('name',)}    


admin.site.register(Page, PageAdmin)
# admin.site.register(Content, ContentAdmin)