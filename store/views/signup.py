from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.views import View
from store.models.customer import Customer

# SingUp View
# Class based view of Signup
class Signup(View):
    def get(self, request):
        return  render(request, 'signup.html')
    
    def post(self, request):
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('passw')
        re_password=request.POST.get('re_pass')
        customer=Customer(name=name,email=email,password=password)
        
        # validation user data 
        value={'name':name,'email':email}
        error_message=None
        if (password!=re_password):
            error_message='Password Not Matched'
        
        # checking if email id is already registered or not  
        # isExists function is defined in customer model
        elif customer.isExists():
            error_message='Email Id Already Registered'

        # Saving new customer data
        if not error_message:
            customer.password=make_password(customer.password)
            customer.register()
            return redirect('Log In')
        else:
            data={'error':error_message,'values':value}
            return render(request, 'signup.html', data)



# function based view of signup
# def signup(request):
#     if request.method=='GET':
#         return  render(request, 'signup.html')
#     else:
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         password=request.POST.get('passw')
#         re_password=request.POST.get('re_pass')
#         customer=Customer(name=name,email=email,password=password)
#         # validation
#         value={'name':name,'email':email}
#         error_message=None
#         if (password!=re_password):
#             error_message='Password Not Matched'
            
#         elif customer.isExists():
#             error_message='Email Id Already Registered'

#         # Saving
#         if not error_message:
#             customer.password=hashers.make_password(customer.password)
#             customer.register()
#             return redirect('Log In')
#         else:
#             data={'error':error_message,'values':value}
#             return render(request, 'signup.html', data)