from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Folower


class RegisterView(SuccessMessageMixin, CreateView):
    template_name = "accounts/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")


# Авторизация предоставлена самим Django
# LoginView
# django.contrib.auth.views.LoginView

# Выход из учетной записи тоже предоставлена самим Django
# LogoutView
# django.contrib.auth.views.LogoutView

class ProfileView(DetailView):
    model = User
    template_name = "accounts/profile.html"
    context_object_name = "profile"



# Если подписан то отписаться если не подписон то подписан JsonResponse
@login_required
@require_POST
def follow_user(request: HttpRequest, user_id: int):
    """
    дома сделать как у лайков и дизлайка
    """
    to_user = get_object_or_404(User, id=user_id)
    user = request.user
    follower, created = Folower.objects.get_or_create(from_user=user, to_user=to_user)
    if not created:
        follower.delete()
        follower = False
    else:
        follower = True
    return JsonResponse(
        {
            "followed":follower
        }
    )


