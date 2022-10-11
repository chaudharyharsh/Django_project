from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.customer import Customer

# Login 
# Class based view of login
class Login(View):
    return_url=None
    
    def get(self, request):
        Login.return_url=request.GET.get('return_url')
        return  render(request, 'login.html')
    
    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('passw')
        customer=Customer.get_customer_by_emailid(email)
        
        error_message=None
        # if customer exist check hashed password with entered password
        if customer:
            
            flag=check_password(password,customer.password )
            if flag:
                request.session['customer']=customer.id
                 
                if Login.return_url:
                   return HttpResponseRedirect(Login.return_url) 
                else:
                    # to empty return_url
                    Login.return_url={}
                    # if password matched redirect to homepage
                    return redirect('Home')
            else:
                #if password is not matched 
                error_message='Email or Password is invalid !!'
        else:
            error_message='Email or Password is invalid !!'

        # if any error occur render login page with error message
        return render(request, 'login.html', {'error':error_message})


# Function based view of login
# def login(request):
#     if request.method=='GET':
#         return  render(request, 'login.html')

#     else:
#         email=request.POST.get('email')
#         password=request.POST.get('passw')
#         customer=Customer.get_customer_by_emailid(email)
        
#         error_message=None
#         # if customer exist check hashed password with entered password
#         if customer:
#             flag=hashers.check_password(password,customer.password )
#             if flag:
#                 # if password matched redirect to homepage
#                 return redirect('Home')
#             else:
#                 #if password is not matched 
#                 error_message='Email or Password is invalid !!'
#         else:
#             error_message='Email or Password is invalid !!'
        
#         # if any error occur render login page with error message
#         return render(request, 'login.html', {'error':error_message})