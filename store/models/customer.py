from django.db import models

class Customer(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=500)
    
    def register(self):
        self.save()

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False

    @staticmethod
    def get_customer_by_emailid(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False