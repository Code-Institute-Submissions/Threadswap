from django.conf.urls import url
from .views import get_items, item_detail, create_item, edit_item, owner_item_detail

urlpatterns = [
    url(r'^$', get_items, name='get_items'),
    url(r'^(?P<pk>\d+)/$', item_detail, name='item_detail'),
    url(r'^profile/(?P<pk>\d+)/$', owner_item_detail, name='owner_item_detail'),
    url(r'^new/$', create_item, name='new_item'),
    url(r'^(?P<pk>\d+)/edit/$', edit_item, name='edit_item')
    ]