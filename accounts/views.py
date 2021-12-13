from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.checks import messages
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.decorators import login_required
from order.views import user_orders
from shop.models import Product
from django.shortcuts import get_object_or_404, render
from .forms import CustomUserCreationForm
from .models import Profile

# Create your views here.

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm



@login_required
def dashboard(request):
    orders = user_orders(request)
    return render(request, "registration/dashboard.html", {"section": "profile", "orders": orders})

    
@login_required
def wishlist(request):
    products = Product.objects.filter(users_wishlist=request.user)
    return render(request, "registration/wishlist.html", {"wishlist": products})


@login_required
def add_to_wishlist(request, id):
    product = get_object_or_404(Product, id=id)
    if product.users_wishlist.filter(id=request.user.id).exists():
        product.users_wishlist.remove(request.user)
    else :
        product.users_wishlist.add(request.user)
    return HttpResponseRedirect(request.META["HTTP_REFERER"])



class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('signin')
    template_name = 'registration/signup.html'

    
""" def SignupView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = CustomUser.objects.get(username=username)
            customer_group = Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)
            success_url = reverse_lazy('signin')
            
    else:
        form = CustomUserCreationForm()
        
    return render(request, 'registration/signup.html', {'form':form}) """


def SigninView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('pages:home')
            else:
                return redirect('signup')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/signin.html', {'form':form})

def SignoutView(request):
    logout(request)
    return redirect('pages:home')


class UserEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = 'registration/edit_profile.html'
    fields = ['id', 'profile_image', 'dob', 'address', 'phone', 'email']
    success_url = reverse_lazy('signin')

    def get_object(self):
        return self.request.user.profile

    def test_func(self):
        return self.request.user.profile

class ProfilePageView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
    success_url = reverse_lazy('signin')

    def get_object(self):
        return self.request.user

    def test_func(self):
        return self.request.user.profile







