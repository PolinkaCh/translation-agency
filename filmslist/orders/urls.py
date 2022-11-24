from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('myorders/', views.myorders, name='myorders'),
    path('neworders/', views.neworders, name='neworders'),
    path('filter/', views.myorders, name='filter')




] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)