import os

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save, post_delete

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
    if instance.first_name and instance.last_name and instance.phone_number and instance.profile_image:
        instance.is_complete = True


@receiver(post_delete, sender=MyWeddingPlannerProfile)
def submission_delete(sender, instance, **kwargs):
    current_profile = MyWeddingPlannerProfile.objects.get (instance.pk)
    current_profile_image_location = os.path.join(settings.MEDIA_ROOT, str(instance.email))
    if current_profile.image:
        current_profile.image.delete()
    if os.path.isdir(current_profile_image_location):
        os.rmdir(current_profile_image_location)
