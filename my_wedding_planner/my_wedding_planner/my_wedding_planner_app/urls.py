from django.urls import path

from my_wedding_planner.my_wedding_planner_app.views import LandingPageView, love_stories

urlpatterns = [
    path('', LandingPageView.as_view(), name='index'),
    path('love_stories/', love_stories, name='love stories'),
]
