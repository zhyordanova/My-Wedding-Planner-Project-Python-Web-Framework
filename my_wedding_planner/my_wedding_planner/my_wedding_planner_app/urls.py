from django.urls import path

from my_wedding_planner.my_wedding_planner_app.views import LandingPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name='index'),
]
