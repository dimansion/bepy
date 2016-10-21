from django.contrib import admin
from showcase.models import UserProfile, UserProject


# class UserProfileAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug':('user',)}

class UserProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}


admin.site.register(UserProfile) 	#,UserProfileAdmin
admin.site.register(UserProject, UserProjectAdmin)
