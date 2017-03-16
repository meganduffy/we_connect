from django.shortcuts import render
from .models import Magazine, Purchase
from django.contrib.auth.decorators import login_required
from django.utils import timezone


@login_required(login_url='/login/')
def all_magazines(request):
    # TODO: If a user is subscribed to a magazine, display the subscription end instead of paypal form
    purchases = Purchase.objects.filter(user=request.user)
    magazines = Magazine.objects.all()
    now = timezone.now()
    return render(request, 'magazines.html', {'magazines': magazines, 'purchases': purchases, 'now': now})

