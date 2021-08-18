from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save

from django.dispatch import receiver

from my_wedding_planner.profiles.models import MyWeddingPlannerProfile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if created:
        profile = MyWeddingPlannerProfile(
            user=instance,
        )

        profile.save()


@receiver(pre_save, sender=MyWeddingPlannerProfile)
def check_is_complete(sender, instance, **kwargs):
    if instance.first_name and instance.last_name and instance.phone_number:
        instance.is_complete = True

    if instance.pk:
        try:
            old_avatar = MyWeddingPlannerProfile.objects.get(pk=instance.pk).profile_image
        except MyWeddingPlannerProfile.DoesNotExist:
            return
        else:
            # try:
            new_avatar = instance.profile_image.url
                # except AttributeError:
            if old_avatar and old_avatar != new_avatar:
                old_avatar.delete(save=False)

# @receiver(post_delete, sender=MyWeddingPlannerProfile)
# def submission_delete(sender, instance, **kwargs):
#     if 'profile_image' in instance.image.url:
#         instance.image.delete(False)
