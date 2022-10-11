from django import template

register=template.Library()

#filter to check whether product is in cart or not
@register.filter(name='currency_symbol')
def currency_symbol(number):
    return '₹ ' + str(number)

@register.filter(name='total')
def total(quantity,price):
    return quantity*price