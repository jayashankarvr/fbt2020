from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': ('first_name', 'last_name', 'username', 'email', 'is_coach','is_manager', 'team')}
            ),
        )    

admin.site.register(CustomUser, CustomUserAdmin)