from django.urls import path
from . import views
from .views import SigninView, SignoutView, UserEditView, ProfilePageView, SignUpView


app_name = 'accounts' 

urlpatterns=[
    #path('create/', SignupView, name='signup'),
    path('signin/', SigninView, name='signin'),
    path('logout/', SignoutView, name='signout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit_profile/<int:pk>/', UserEditView.as_view(), name='edit_profile'),
    path("dashboard", views.dashboard, name="dashboard"),
    path('profile/<int:pk>/', ProfilePageView.as_view(), name='show_profile'),
    path("wishlist", views.wishlist, name="wishlist"),
    path('wishlist/add_to_wishlist/<int:id>', views.add_to_wishlist, name='user_wishlist'),
]