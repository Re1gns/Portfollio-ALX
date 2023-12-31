from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_user, name="login"),
    path('logout', views.logout_user, name='logout'),
    path('signup', views.register, name='signup'),
    path('cancel-membership/', views.cancel_membership, name='cancel_membership'),
    path('profile/<user_id>', views.user_profile, name='profile'),

]
