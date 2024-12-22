from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Profile

def landing_view(request):
    return render(request, "users/landing.html")

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)  # Ensure profile is created
            login(request, user)
            return redirect("exercise")
    else:
        form = UserCreationForm()
    return render(request, "users/signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})

@login_required
def exercise_view(request):
    if request.method == "POST":
        # Retrieve form data
        stress_level = request.POST.get("stress_level")
        focus_difficulty = request.POST.get("focus_difficulty")
        anxiety_level = request.POST.get("anxiety_level")
        interest_loss = request.POST.get("interest_loss")
        sleep_disturbance = request.POST.get("sleep_disturbance")

        # Map responses to numerical values for calculations (0 = low, 1 = medium, 2 = high)
        stress_map = {"low": 0, "medium": 1, "high": 2}
        focus_map = {"low": 0, "medium": 1, "high": 2}
        anxiety_map = {"low": 0, "medium": 1, "high": 2}
        interest_map = {"low": 0, "medium": 1, "high": 2}
        sleep_map = {"low": 0, "medium": 1, "high": 2}

        # Fetch or create the user's profile
        profile, created = Profile.objects.get_or_create(user=request.user)
        
        # Update profile with mapped values
        profile.stress_level = stress_map.get(stress_level, 0)
        profile.focus_level = focus_map.get(focus_difficulty, 0)
        profile.anxiety_level = anxiety_map.get(anxiety_level, 0)
        profile.interest_loss = interest_map.get(interest_loss, 0)
        profile.sleep_disturbance = sleep_map.get(sleep_disturbance, 0)
        
        # Save the profile
        profile.save()
        
        # Redirect to the dashboard or another appropriate page
        return redirect("dashboard")
    
    # Render the exercise page if the request is GET
    return render(request, "users/exercise.html")
@login_required
def dashboard_view(request):
    try:
        profile = Profile.objects.get(user=request.user)  # Access the Profile object
    except Profile.DoesNotExist:
        profile = None  # Handle case where profile does not exist
    return render(request, "users/dashboard.html", {
        "Profile": profile
    })
@login_required
def logout_view(request):
    logout(request)
    return render(request, "users/logout.html")

@login_required
def game1_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == "POST":
        # Add 10 coins each time the button is pressed
        profile.coins=profile.coins + 10
        profile.save()
    
    return render(request, "users/game1.html", {"profile": profile})
@login_required
def game2_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == "POST":
        # Add 10 coins each time the button is pressed
        profile.coins += 10
        profile.save()
    
    return render(request, "users/game2.html", {"profile": profile})

