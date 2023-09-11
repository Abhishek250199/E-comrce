
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',home,name='home'),
    path('gallary/',gallary,name='gallary'),
    path('contact/',contact,name='contact'),
    path('cart/',cart,name='cart'),
    path('search/',search,name='search'),
    # path('login/',login,name='login'),
    # path('signup/',signup,name='signup'),
    # path('logout/',logout,name='logout'),
    path('payment/',payment,name='payment'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
