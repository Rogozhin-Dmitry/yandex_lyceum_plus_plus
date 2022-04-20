from django.contrib import admin
from users.models import Profile, CustomUser


class ProfileInlined(admin.TabularInline):
    model = Profile
    can_delete = False
    fields = ('birthday', )


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", 'last_name')
    inlines = (ProfileInlined,)
    exclude = ('username',)
