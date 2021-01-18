from django.urls import path
from django.utils.translation import gettext_lazy as _
from . import views

app_name = 'order'

urlpatterns = [
    path(_('create/'), views.order_create, name='order_create'),
    path(_('apply/'), views.coupon_apply, name='apply'),
    path('admin/order/<int:order_id>', views.admin_order_detail, name='admin_order_detail'),
]