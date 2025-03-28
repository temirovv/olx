from django.db import models
import uuid

class CategoryModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    title = models.CharField(max_length=255) 
    description = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.title  
