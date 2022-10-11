from django.shortcuts import render,redirect
from django.views import View
from store.models.item import Product
class Cart(View):
    def get(self, request):
        ids=list(request.session.get('cart').keys())
        cartprod=Product.get_all_item_by_id(ids)
        return  render(request, 'cart.html',{'products':cartprod})