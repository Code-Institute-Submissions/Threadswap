from django.conf.urls import url
from .views import get_items, item_detail, create_or_edit_item

urlpatterns = [
    url(r'^$', get_items, name='get_items'),
    url(r'^(?P<pk>\d+)/$', item_detail, name='item_detail'),
    url(r'^new/$', create_or_edit_item, name='new_item'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_item, name='edit_item')
    ]