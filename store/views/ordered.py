from django.shortcuts import render,redirect
from django.views import View
from store.models.item import Product
from store.models.customer import Customer
from store.models.order import Order
# one way of applying middleware
# from store.middleware.auth import auth_middleware
# from django.utils.decorators import method_decorator


class Ordered(View):
    # @method_decorator(auth_middleware)
    def get(self, request):
        cust=request.session.get('customer')
        odr=Order.get_orders_by_customerid(cust)
        return render(request, 'ordered.html',{'order':odr})