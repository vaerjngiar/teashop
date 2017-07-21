from django.conf.urls import url
from .views import CartAdd, CartRemove, CartDetail
#from . import views


urlpatterns = [
    url(r'^$', CartDetail.as_view(), name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', CartAdd.as_view(), name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', CartRemove.as_view(), name='cart_remove'),


    # url(r'^$', views.cart_detail, name='cart_detail'),
    # url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    # url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
]
