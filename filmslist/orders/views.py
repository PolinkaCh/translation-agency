from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

# Create your views here.

from .models import Translators, TranslationTypes, MovieType, LanguagePairs, Order, Post


def index(request):
    context = {
    }
    return render(request,'index.html', context)

def profile(request):
    return render(request, 'profile.html')

def myorders(request):
    order = Order.objects.order_by('receipt_date')
    sum=0
    for el in order:
        sum += el.rate * el.duration

    months = Order.objects.values('deadline')

    queryset = Order.objects.filter(deadline__in=request.GET.getlist('deadline'))

    #context = {'orders': Order.objects.filter(Order.translator == request.user)}
    return render(request, 'myorders.html', {'order': order, 'sum': sum, 'months': months, 'queryset': queryset})

def neworders(request):
    newOrder = Post.objects.order_by('date_posted')
    return render(request, 'neworders.html', {'newOrder': newOrder})

def pagi(request):
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(Post, 1)
    page = paginator.get_page(page_number)
    return render(request, 'neworders.html', {'page': page})
