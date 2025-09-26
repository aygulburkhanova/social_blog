from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, DetailView
from django.core.exceptions import PermissionDenied
from accounts.forms import UserChangeForm, UserCreationForm, ProfileForm
from accounts.models import Follower, Profile


from collections_app.forms import AddToCollectionForm
from collections_app.models import Collection
from django.views.generic import TemplateView, UpdateView

class RegisterView(SuccessMessageMixin, CreateView):
    template_name = "accounts/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")


# Авторизация предоставлена самим Django
# LoginView
# django.contrib.auth.views.LoginView

# Выход из учетной записи предоставлена самим Django
# LogoutView
# django.contrib.auth.views.LogoutView

class ProfileView(DetailView):
    model = User
    template_name = "accounts/profile.html"
    context_object_name = "profile"


    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs) 
        context["avatar"] = self.get_object().profile.avatar
        context["collection_form"] = AddToCollectionForm(
            user=self.request.user) if self.request.user.is_authenticated else None
        context["collections"] = Collection.objects.filter(
            user=self.request.user) if self.request.user.is_authenticated else None
        return context



class SettingsView(TemplateView):
    template_name = "accounts/settings.html"
    

class UserUpdateView(SuccessMessageMixin, UpdateView):
    template_name = "accounts/form.html"
    form_class = UserChangeForm
    model = User
    success_url = reverse_lazy("index")

    def get_object(self, queryset = ...):
        return self.request.user
    

class ProfileUpdateView(SuccessMessageMixin, UpdateView):
    template_name = "accounts/form.html"
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy("index")


    def get_object(self, queryset = ...):
        return self.request.user.profile



# Если подписан то отписаться если не подписан то подписаться
@login_required
@require_POST
def follow_user(request: HttpRequest, user_id: int):
    to_user = get_object_or_404(User, id=user_id) # Ramiz
    user = request.user # Aygul
    follower, created = Follower.objects.get_or_create(from_user=user, to_user=to_user)
    if not created:
        follower.delete()
        followed = False
    else:
        followed = True
    return JsonResponse(
        {
            "followed": followed
        }
    )




