from django.db import models

class Categorie(models.Model):
    name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

    @staticmethod
    def get_all_category():
        return Categorie.objects.all()