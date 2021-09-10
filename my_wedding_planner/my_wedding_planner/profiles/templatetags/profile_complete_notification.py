from django import template

from my_wedding_planner.profiles.models import MyWeddingPlannerProfile

register = template.Library()


@register.inclusion_tag('shared/tags/profile_complete_notification.html', takes_context=True)
def profile_complete_notification(context):
    is_complete = True

    if context.request.user.id:
        profile = MyWeddingPlannerProfile.objects.get(pk=context.request.user.id)
        is_complete = profile.is_complete

    return {
        'is_complete': is_complete,
    }
