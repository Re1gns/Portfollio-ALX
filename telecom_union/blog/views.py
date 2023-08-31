from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment, UserProfile, ContactMessage, Event, JoinApplication
from .forms import ContactForm, CommentForm, JoinForm

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
                    messages.warning(request, 'You\'re already a member!')
                else:
                    return redirect('join')  # Redirect to the join page for registered users
        return render(request, 'blog/membership.html')
    else:
        if request.method == 'POST':
            action = request.POST.get('action')

            if action == 'join':
                messages.warning(request, 'Please log in first to become a member')
        return render(request, 'blog/membership.html')

def post_list(request):
    author = "admin"
    posts = Post.objects.all().order_by('-created_at')
    context = {"posts": posts, "author": author}
    return render(request, "blog/post_list.html", context=context)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                form = CommentForm()  # Reset the form
                return redirect('post_detail', slug=slug)  # Redirect to fix the resubmitting issue
        else:
            messages.warning(request, 'Please log in first to add a comment')

    else:
        form = CommentForm()

    comments = Comment.objects.filter(post=post)

    context = {'post': post, 'comments': comments, 'form': form}
    return render(request, 'blog/post_detail.html', context=context)

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = form.cleaned_data['subject']

            ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)

            messages.success(request, 'We\'ve received your message, thank you!')
            return redirect('contact-us')
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})


def faqs(request):
    return render(request, "blog/faqs.html")

def terms_of_service(request):
    return render(request, "blog/terms.html")


def event_list(request):
    event_date = "Starts On"
    events = Event.objects.all().order_by('-created_at')
    context = {"events": events, "event_date": event_date}
    return render(request, "blog/event_list.html", context=context)

def event_detail(request, slug):
    event = Event.objects.get(slug=slug)
    context = {'event': event}
    return render(request, 'blog/event_detail.html', context=context)

def join(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            if not user_profile.is_member:
                user_profile.is_member = True
                user_profile.save()
                messages.success(request, 'You\'ve become a member. Congratulations!')


                # Save form data to the database
                join_application = JoinApplication(
                    user=request.user,
                    full_name=form.cleaned_data['full_name'],
                    age=form.cleaned_data['age'],
                    gender=form.cleaned_data['gender'],
                    address=form.cleaned_data['address'],
                    city=form.cleaned_data['city'],
                    postal_code=form.cleaned_data['postal_code'],
                    phone_number=form.cleaned_data['phone_number'],
                    email=form.cleaned_data['email'],
                    employment_status=form.cleaned_data['employment_status'],
                    job_title=form.cleaned_data['job_title'],
                    how_heard=form.cleaned_data['how_heard'],
                    why_join=form.cleaned_data['why_join']
                )
                join_application.save()
                return redirect('success')

            else:
                messages.warning(request, 'You\'re already a member!')
                return redirect('join')  # Redirect back to the join page
        else:
            messages.warning(request, 'Please enter a valid email address!')
            return redirect('join')
    else:
        form = JoinForm()
        return render(request, 'blog/join.html', {'form': form})

@login_required
def success(request):
    return render(request, "blog/success.html")
