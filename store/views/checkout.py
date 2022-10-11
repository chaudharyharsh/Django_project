from django.shortcuts import render,redirect
from django.views import View
from store.models.item import Product
from store.models.customer import Customer
from store.models.order import Order

class Checkout(View):
    def post(self, request):
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        customer=request.session.get('customer')
        cart=request.session.get('cart')
        product=Product.get_all_item_by_id(list(cart.keys()))
       

        for p in product:
            odr=Order(customer=Customer(id=customer),
                    product=p,
                    quantity=cart.get(str(p.id)),
                    price=p.price,
                    address=address,
                    phone=phone)

            odr.placeorder()
        request.session['cart']={}
        return redirect('Cart')