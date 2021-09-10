from django.contrib.auth import get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DeleteView

from my_wedding_planner.profiles.forms import PlannerProfileForm
from my_wedding_planner.profiles.models import MyWeddingPlannerProfile
from my_wedding_planner.tasklist.models import TaskList

UserModel = get_user_model()


@login_required
def profile_details(request):
    profile = MyWeddingPlannerProfile.objects.get(pk=request.user.id)

    if request.method == 'POST':
        form = PlannerProfileForm(
            request.POST,
            request.FILES,
            instance=profile,
        )

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = PlannerProfileForm(instance=profile)

    user_tasks = TaskList.objects.filter(user_id=request.user.id)

    context = {
        'form': form,
        'tasks': user_tasks,
        'profile': profile,
    }

    return render(request, 'profiles/dashboard_profiles.html', context)


class DeleteProfileView(DeleteView):
    model = UserModel
    template_name = 'profiles/delete_profile.html'

    def get_success_url(self):
        logout(self.request)
        return reverse('index')
