from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.carts.models import ProductCard
from apps.general.models import General


@login_required
def checkout(request):
    carts = ProductCard.objects.filter(user=request.user).select_related('product')
    if not carts:
        return redirect('carts:cart')

    try:
        shipping_percent = General.objects.first().shipping_percent
    except AttributeError:
        shipping_percent = 0

    total_cart = sum([cart.quantity * cart.product.price for cart in carts])

    coupon_discount_percent = request.session.get('coupon_data', {}).get('discount_percent', 0)

    total_sum = total_cart - total_cart*coupon_discount_percent/100 + total_cart*shipping_percent/100

    context = {'carts': carts,
               'page': 'pages',
               'shipping_percent': shipping_percent,
               'total_cart': total_cart,
               'total_sum': total_sum,
               }
    return render(request, template_name='checkout.html', context=context)