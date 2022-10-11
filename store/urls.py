from django.urls import path
from .views import index,signup,login,cart,logout,checkout,ordered,aboutus
from store.middleware.auth import auth_middleware


urlpatterns = [
    
    path("", index.Index.as_view(), name='Home'),
    path("signup", signup.Signup.as_view(), name='Signup'),
    path("login",login.Login.as_view(), name='Login'),
    path("logout",logout.Logout.as_view(), name='Logout'),
    path("cart",cart.Cart.as_view(), name='Cart'),
    path('checkout',checkout.Checkout.as_view() , name='checkout'),
    path('ordered',auth_middleware(ordered.Ordered.as_view()) , name='ordered'),
    path('aboutus',aboutus.Aboutus.as_view() , name='aboutus'),
    path('contactus',aboutus.Contactus.as_view() , name='contactus'),

    


]