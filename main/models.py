from django.db import models
from .utils import valid_prise

# Create your models here.
class Category(models.Model):
      title = models.CharField(max_length=255, verbose_name="Категория")
      created_at = models.DateTimeField(auto_now_add=True,
                                        verbose_name="Дата создания")

      def __str__(self):
            return self.title

      class Meta:
            verbose_name = "Категория"
            verbose_name_plural = "Категории"

class Product(models.Model):
      image = models.ImageField(upload_to='product/')
      title = models.CharField(max_length=250, verbose_name="Название")
      description = models.TextField(verbose_name="Опсание")
      price = models.CharField(default=10.0, verbose_name="Цена",
            validators=[valid_prise], max_length=255)
      category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                   verbose_name="Категория")
      created_at = models.DateTimeField(auto_now_add=True,
                                        verbose_name="Дата создания")

      def __str__(self) -> str:
            return f"{self.title} - {self.category} - {self.created_at}"

      class Meta:
            verbose_name = "Товар"
            verbose_name_plural = "Товары"


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


