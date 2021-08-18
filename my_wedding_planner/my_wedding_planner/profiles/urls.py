from django.urls import path

from my_wedding_planner.profiles.views import profile_details, DeleteProfileView

urlpatterns = [
    path('dashboard/', profile_details, name='dashboard profile'),
    # path('edit_info', edin_profile_info, name='edit profile info'),
    path('delete/<int:pk>', DeleteProfileView.as_view(), name='delete profile'),
]
