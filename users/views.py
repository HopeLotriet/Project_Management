from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm, CustomLoginForm
from .models import CustomUser
from projects.models import StudentProfile


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            role = request.POST.get('role')
            user.role = role
            user.save()

            # Automatically create StudentProfile if role is student
            if role == 'student':
                supervisor = CustomUser.objects.filter(role='admin').first()
                StudentProfile.objects.create(user=user, supervisor=supervisor)

            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    form = CustomLoginForm(data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)

        # Redirect based on user role
        if user.role == 'admin':
            return redirect('overview') # Admin
        elif user.role == 'manager':
            return redirect('manager_dashboard') # Project Manager
        elif user.role == 'student':
            return redirect('student_dashboard')  # Student
        else:
            return redirect('dashboard') # Staff
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
