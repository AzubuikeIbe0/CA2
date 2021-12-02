from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import  UpdateView, DetailView
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile


# Create your views here.

def SignupView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = CustomUser.objects.get(username=username)
            customer_group = Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})



def SigninView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('shop:allProdCat')
            else:
                return redirect('signup')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/signin.html', {'form':form})

def SignoutView(request):
    logout(request)
    return redirect('signin')

""" class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html' """

class UserEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = 'registration/edit_profile.html'
    fields = ['user', 'profile_image', 'dob', 'address', 'phone', 'email']
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user.profile

    def test_func(self):
        return self.request.user.profile

class ProfilePageView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

    def test_func(self):
        return self.request.user.profile





