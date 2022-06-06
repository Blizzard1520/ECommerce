from django.db import models
from django.urls import reverse
from django.db.models import Model


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    category_image = models.ImageField(upload_to='photos/categories/', blank=True)

    USERNAME_FIELD='category_name'
    REQUIRED_FIELDS=['category_name', 'description']
    

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name