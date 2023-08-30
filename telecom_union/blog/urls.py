from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('home/', views.home_page, name='home'),
    path('news/', views.post_list, name='post_list'),
    path('events/', views.event_list, name='events'),
    path('about-us/', views.about_us, name='about-us'),
    path('membership/', views.membership, name='membership'),
    path('members/join/', views.join, name='join'),
    path('members/success/', views.success, name='success'),
    path('faqs/', views.faqs, name='faqs'),
    path('terms/', views.terms_of_service, name='terms'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('news/<slug:slug>/', views.post_detail, name="post_detail"),
    path('events/<slug:slug>/', views.event_detail, name="event_detail"),
]