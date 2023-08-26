from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment, UserProfile

# Create your views here.


def home_page(request):
    featured_posts = Post.objects.filter(featured=True).order_by('-created_at')
    context = {"featured_posts": featured_posts, "author": "admin"}
    return render(request, "blog/index.html", context=context)

def about_us(request):
    return render(request, "blog/about.html")

def contact_us(request):
    return render(request, "blog/contact.html")

def membership(request):
    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)

        if request.method == 'POST':
            action = request.POST.get('action')

            if action == 'join':
                if user_profile.is_member:
                    messages.info(request, 'You\'re already a member!')
                    return redirect('membership')

                user_profile.is_member = True
                user_profile.save()
                messages.success(request, 'You\'ve become a member. Congratulations!')
                return redirect('membership')

        return render(request, 'blog/membership.html')
    else:
        if request.method == 'POST':
            action = request.POST.get('action')

            if action == 'join':
                messages.info(request, 'Please log in first to become a member')
        return render(request, 'blog/membership.html')

def post_list(request):
    author = "admin"
    posts = Post.objects.all().order_by('-created_at')
    context = {"posts": posts, "author": author}
    return render(request, "blog/post_list.html", context=context)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context=context)
