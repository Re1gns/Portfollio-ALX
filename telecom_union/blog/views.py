from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, UserProfile

# Create your views here.


def home_page(request):
    featured_posts = Post.objects.filter(featured=True).order_by('-created_at')
    context = {"featured_posts": featured_posts, "author": "admin"}
    return render(request, "blog/index.html", context=context)

def about_us(request):
    return render(request, "blog/about.html")

def post_list(request):
    author = "admin"
    posts = Post.objects.all().order_by('-created_at')
    context = {"posts": posts, "author": author}
    return render(request, "blog/post_list.html", context=context)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context=context)
