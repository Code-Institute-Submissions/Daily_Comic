from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Userprofiles
from .forms import ProfileForm
from checkout.models import Order


def theProfile(request):
    profile = get_object_or_404(Userprofiles, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Successfully updated your details!')

    orders = profile.orders.all()
    template = 'profiles/theprofile.html'
    form = ProfileForm(instance=profile)
    context = {
        'form': form,
        'orders': orders,
        'on_profile': True,
    }
    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
