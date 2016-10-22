from django.contrib import admin
from showcase.models import UserProfile, UserProject


class UserProjectInline(admin.TabularInline):
    model = UserProject
    prepopulated_fields = {'slug':('title',)}
    extra = 0


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')
    fieldsets = [
		(None,               {'fields': [ 'user', 'name', 'profile_image']}),
	]
    inlines = [UserProjectInline]


admin.site.register(UserProfile, UserProfileAdmin)
# admin.site.register(UserProject, UserProjectAdmin)
