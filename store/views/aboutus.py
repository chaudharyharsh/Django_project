from django.shortcuts import render,redirect
from django.views import View

class Aboutus(View):
    # @method_decorator(auth_middleware)
    def get(self, request):
        return render(request, 'aboutus.html')

class Contactus(View):
    # @method_decorator(auth_middleware)
    def get(self, request):
        return render(request, 'contactus.html')