from django.db import models

# # Create your models here.
class Category(models.Model):
    category_item = [
        ('Cleaning ', 'Cleaning'),
        ('Panatary ', 'Panatary'),
        ('General', 'General'),
    ]
    category_name = models.CharField(
        max_length=20,
        choices=category_item,
        default='Cleaning',
    )
    # category_name=models.CharField(max_length=20)
    # checked = models.BooleanField()
 
    def __str__(self):
        return self.category_name

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categories')
    product_name=models.CharField(max_length=50)
    product_img=models.ImageField(upload_to='product_img',null=True,blank=True)
    product_img_icon=models.ImageField(upload_to='product_img_icon',null=True,blank=True)
    price=models.PositiveIntegerField()
    quantity_label=models.CharField(max_length=20)

  
    def __str__(self):
        return self.product_name
