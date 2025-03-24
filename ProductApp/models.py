from django.db import models
import uuid

class ProductModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    title = models.CharField(max_length=255) 
    description = models.TextField() 
    price = models.IntegerField()  
    old_price = models.IntegerField(null=True, blank=True)  
    category = models.CharField(max_length=50) 
    created_at = models.DateTimeField(auto_now_add=True)  
    image = models.ImageField(upload_to='products/', null=True , blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1200)
    user = models.CharField(max_length=40)
    rating = models.PositiveIntegerField(null=True, blank=True)

