from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from my_wedding_planner.accounts.models import MyWeddingPlannerUser


@admin.register(MyWeddingPlannerUser)
class MyWeddingPlannerAdmin(UserAdmin):
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    ordering = ('email',)
    search_fields = ('email', 'phone_number')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined', 'date_changed')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    readonly_fields = ('date_joined', 'date_changed', 'last_login')
