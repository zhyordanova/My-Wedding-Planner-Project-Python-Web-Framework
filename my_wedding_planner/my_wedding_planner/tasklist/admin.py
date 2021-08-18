from django.contrib import admin

from my_wedding_planner.tasklist.models import TaskList


@admin.register(TaskList)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'likes_count')

    def likes_count(self, obj):
        return obj.like_set.count()
