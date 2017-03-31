from django.contrib import messages, auth
from accounts.models import User
from accounts.forms import UserRegistrationForm, UserLoginForm, UserProfileForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from magazines.models import Purchase, Magazine
from django.utils import timezone
from django.http import HttpResponse


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                messages.success(request, "You have successfully registered")
                return redirect(reverse('profile'))

            else:
                messages.error(request, "unable to log you in at this time!")

    else:
        form = UserRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'register.html', args)


@login_required(login_url='/login/')
def profile(request):
    purchases = Purchase.objects.filter(user=request.user
                                        ).exclude(subscription_end__lte=timezone.now()
                                        ).order_by('subscription_end')
    magazines = {p.magazine for p in purchases}
    return render(request, 'profile.html', {'purchases': purchases, 'magazines': magazines})


@login_required(login_url='/login/')
def edit_profile(request):

    if request.method == "POST":
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            return redirect(profile)
    else:
        profile_form = UserProfileForm()
    return render(request, 'profileform.html', {'profile_form': profile_form})


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password'))

            if user is not None:
                user.previous_login = user.last_login
                user.save()
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was not recognised")

    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'login.html', args)


def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect(reverse('index'))
