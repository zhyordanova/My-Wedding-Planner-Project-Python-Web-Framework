# from django.contrib.auth.backends import ModelBackend
# from django.db.models import Q
# from django.contrib.auth import get_user_model
#
#
# class EmailBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         user_model = get_user_model()
#         try:
#             user = user_model.objects.get(Q(email__iexact=username))
#         except user_model.DoesNotExist:
#             return None
#         else:
#             if user.check_password(password) and self.user_can_authenticate(user):
#                 return user
#
#     def get_user(self, user_id):
#         user_model = get_user_model()
#         try:
#             user = user_model.objects.get(pk=user_id)
#         except user_model.DoesNotExist:
#             return None
#
#         return user if self.user_can_authenticate(user) else None