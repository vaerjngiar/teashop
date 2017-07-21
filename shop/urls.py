from django.conf.urls import url
from .views import ProductList, ProductDetail
from . import views


urlpatterns = [
    url(r'^$', ProductList.as_view(), name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', ProductList.as_view(), name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', ProductDetail.as_view(), name='product_detail'),


    # url(r'^$', views.product_list, name='product_list'),
    # url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    #url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),

]
