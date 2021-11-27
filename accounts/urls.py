from django.urls import path
from .views import UserEditView, ProfilePageView
from django.urls import path
from shop import views
from .views import SignupView, SigninView, SignoutView

urlpatterns = [
    path('create/', SignupView, name='signup'),
    path('login/', SigninView, name='signin'),
    path('logout/', SignoutView, name='signout'),
    path('edit_profile/<int:pk>/', UserEditView.as_view(), name='edit_profile'),
    path('profile/<int:pk>/', ProfilePageView.as_view(), name='show_profile'),
]

""" urlpatterns=[
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit_profile/<int:pk>/', UserEditView.as_view(), name='edit_profile'),
    path('profile/<int:pk>/', ProfilePageView.as_view(), name='show_profile'),
]  """