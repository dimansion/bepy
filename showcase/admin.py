from django.contrib import admin
from showcase.models import UserProfile, UserProject


class UserProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('user',)}


admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(UserProject)
