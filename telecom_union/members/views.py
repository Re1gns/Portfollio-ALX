from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import RegisterUserForm
from blog.models import UserProfile, JoinApplication
from django.urls import reverse

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.warning(request, ("There Was An Error Logging In, Please Try Again..."))	
			return redirect('login')	


	else:
		return render(request, 'auth/login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, ("You Were Logged Out!"))
	return redirect('home')


def register(request):
	if request.method == "POST":
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("Registration Successful!"))
			return redirect('home')
	else:
		form = RegisterUserForm()

	return render(request, 'auth/register.html', {
		'form':form,
		})

def user_profile(request, user_id):
    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        is_member = user_profile.is_member  # Get the is_member status
        
        profile = User.objects.get(pk=user_id)
        return render(request, 'auth/profile.html', {
            "profile": profile, "is_member": is_member,
        })  # temp view
    
def cancel_membership(request):
    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        if user_profile.is_member:
            user_profile.is_member = False
            user_profile.save()

            # Delete the user's JoinApplication
            JoinApplication.objects.filter(user=request.user).delete()

            messages.success(request, "You've canceled your membership successfully")
            user_id = request.user.id  # Get the user id
            profile_url = reverse('profile', args=[user_id])
            return redirect(profile_url)  # Redirect back to the user's profile page

    return redirect('login')
