from django.shortcuts import render
from django.views.generic import TemplateView


class LandingPageView(TemplateView):
    template_name = 'my_wedding_planner_app/index.html'


def love_stories(request):
    return render(request, 'my_wedding_planner_app/love_stories_carousel.html')
