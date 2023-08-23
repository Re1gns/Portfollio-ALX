from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('home/', views.home_page, name='home'),
    path('news/', views.post_list, name='post_list'),
    path('about_us/', views.about_us, name='about-us'),
    path('<slug:slug>/', views.post_detail, name="post_detail"),
    # path('membership/', views.membership, name='membership'),
    # path('faqs/', views.faqs, name='faqs'),
    # path('contact-us/', views.contact_us, name='contact-us'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

]