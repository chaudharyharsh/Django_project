from django.db import models
from .category import Categorie
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    category=models.ForeignKey(Categorie, on_delete=models.CASCADE, default='')
    desc=models.TextField(max_length=300, default='', null=True, blank=True)
    images=models.ImageField(upload_to ='uploads\products')

    @staticmethod
    def get_all_item():
        return Product.objects.all()

    @staticmethod
    def get_all_item_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_item()

    @staticmethod
    def get_all_item_by_id(ids):
        return Product.objects.filter(id__in=ids)