from django import template

register=template.Library()

#filter to check whether product is in cart or not
@register.filter(name='in_cart')
def in_cart(prod,cart):
    keys=cart.keys()
    for id in keys:
        if int(id)==prod.id:
            return True
    return False

#filter to count product quantity in cart
@register.filter(name='cart_count')
def cart_count(prod,cart):
    keys=cart.keys()
    for id in keys:
        if int(id)==prod.id:
            return cart.get(id)
    return 0

# filter to get Total amount of products
@register.filter(name='prod_total')
def prod_total(prod,cart):
    return prod.price * cart_count(prod, cart)

# filter to get cart total
@register.filter(name='cart_total')
def cart_total(prod,cart):
    sum=0
    for all in prod:
        sum+= prod_total(all, cart)
    return sum