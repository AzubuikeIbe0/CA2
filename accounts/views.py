from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import CustomUserCreationForm
from .models import Profile

# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class UserEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = 'registration/edit_profile.html'
    fields = ['id', 'profile_image', 'dob', 'address', 'phone', 'email']
    success_url = reverse_lazy('login')

    def get_object(self):
        return self.request.user.profile

    def test_func(self):
        return self.request.user.profile

class ProfilePageView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
    success_url = reverse_lazy('login')

    def get_object(self):
        return self.request.user

    def test_func(self):
        return self.request.user.profile

