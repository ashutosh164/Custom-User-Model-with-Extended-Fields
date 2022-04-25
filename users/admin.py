from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea


class UserAdminConfig(UserAdmin):
    ordering = ['-start_date']
    search_fields = ('email','first_name','user_name')
    list_display = ('email', 'user_name', 'first_name', 'is_active','is_staff')
    fieldsets = (
        (None, {'fields':('email','user_name','first_name')}),
        ('Permissions',{'fields':('is_staff', 'is_active')}),
        ('Personal',{'fields':('about',)}),
    )

    formfield_overrides = {
        NewUser.about: {'widget': Textarea(
                           attrs={'rows': 1,
                                  'cols': 40,
                                  'style': 'height: 1em;'})},
    }

    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('email','user_name','first_name','password1','password2',)
                }),
    )


admin.site.register(NewUser, UserAdminConfig)
