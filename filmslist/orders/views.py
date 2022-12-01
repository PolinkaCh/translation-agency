from django.shortcuts import render
from .models import Translators, Order, Post


def index(request):       #рендер приветственной страницы
    return render(request,'index.html')

def profile(request):     #рендер профиля
    return render(request, 'profile.html')

def myorders(request):       #рендер страницы со взятыми заказами
    user = request.user
    translator = Translators.objects.get(user_name=user)
    order = Order.objects.filter(translator=translator)
    if order is not None:
        order = order.order_by('receipt_date')      #вывод всех выполненных пользователем заказов
        queryset = order
    sum = 0
    for el in order:
        sum += el.rate * el.duration

    months = order.values('deadline')            #фильтр по месяцам
    mo = list()
    m = request.GET.getlist('month')
    if len(m) != 0:
        for mon in m:
            mo.append(mon.split(' ')[0].replace('.', ''))

        queryset = list()
        for o in order:
            if o.deadline.strftime("%b") in mo:
                queryset.append(o)

    return render(request, 'myorders.html', {'order': order, 'sum': sum, 'months': months,
                                             'queryset': queryset, "user": user})

def neworders(request):            #рендер страницы с новыми заказами
    newOrder = Post.objects.order_by('date_posted')
    return render(request, 'neworders.html', {'newOrder': newOrder})





