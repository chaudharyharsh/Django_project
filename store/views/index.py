from django.shortcuts import render,redirect
from django.views import View
# importing models
from store.models.item import Product
from store.models.category import Categorie

# Index Page View
class Index(View):
    def post(self, request):
        prod=request.POST.get('product_id')
        remove=request.POST.get('remove_product')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(prod)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(prod)
                    else:
                        cart[prod]=quantity-1
                else: 
                    cart[prod]=quantity+1
            else:
                cart[prod]=1
        else:
            cart={}
            cart[prod]=1

        request.session['cart']=cart
        # print('cart is:',request.session['cart'])
        return redirect('Home')



    def get(self,request):
        
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}
                    
        prod=None
        cate=Categorie.get_all_category()
        
        #Filter by category_id 
        categoryID=request.GET.get('category')
        if categoryID:
            prod=Product.get_all_item_by_categoryid(categoryID)
        else:
            prod=Product.get_all_item()

        # To show filtered Data
        data={}
        data['products']=prod
        data['category']=cate
        # print('you are :',request.session.get('email'))
        return  render(request, 'index.html',data)