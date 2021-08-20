from django.contrib import admin

from my_wedding_planner.profiles.models import MyWeddingPlannerProfile


@admin.register(MyWeddingPlannerProfile)
class MyWeddingPlannerProfileAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    list_display = (
        'first_name',
        'last_name',
        'age',
        'phone_number',
        'profile_image',
        'is_complete',
        'user',
    )
    search_fields = (
        'first_name',
        'last_name',
    )
    list_filter = (
        'first_name',
        'last_name',
        'age',
        'phone_number',
        'profile_image',
        'is_complete',
        'user',
    )
    fieldsets = (
        ('User info', {
            'fields': (
                'first_name',
                'last_name',
                'age',
                'phone_number',
                'profile_image',
                'is_complete',
                'user',
            )}),
    )
