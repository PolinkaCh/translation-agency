from django.shortcuts import render


# Create your views here.

from .models import Translators, Order, Post


def index(request):
    return render(request,'index.html')

def profile(request):
    return render(request, 'profile.html')

def myorders(request):
    user = request.user
    translator = Translators.objects.get(user_name=user)
    order = Order.objects.filter(translator=translator).order_by('receipt_date')
    sum = 0
    for el in order:
        sum += el.rate * el.duration

    months = order.values('deadline')
    queryset = Order.objects.filter(deadline__in=request.GET.getlist('months'))

    return render(request, 'myorders.html', {'order': order, 'sum': sum, 'months': months, 'queryset': queryset, "user": user})

def neworders(request):
    newOrder = Post.objects.order_by('date_posted')
    return render(request, 'neworders.html', {'newOrder': newOrder})





