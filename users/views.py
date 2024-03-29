from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, ListView

from payments.views import is_admin
from users.forms import UserRegisterForm, UserForm
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):

    def get_success_url(self):
        return reverse_lazy('payments:home')


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm
    template_name = 'users/user_form.html'

    def get_success_url(self):
        return reverse_lazy('payments:home')

    def get_object(self, queryset=None):
        return self.request.user


@method_decorator(user_passes_test(is_admin), name='dispatch')
class UserListView(ListView, LoginRequiredMixin):
    model = User
