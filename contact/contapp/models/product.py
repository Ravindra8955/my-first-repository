from django.db import models
from django.utils.safestring import mark_safe
from django.utils.html import format_html


class Category(models.Model):
    category_name = models.CharField(max_length = 50)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)
    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.category_name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name= models.CharField(max_length=100)
    product_description=models.TextField()
    product_image=models.FileField(upload_to='product_image',null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    def image_tag(self):
        if self.product_image:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' & self.product_image.url)
        else:
            return 'no image found'
        image_tag.short_description = 'Image'

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.product_name

class ProductImage(models.Model):
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.FileField(upload_to='product_image')

    class Meta:
        db_table = 'product_images'

    def __str__(self):
        return self.product.product_name

class ContactInfo(models.Model):

    mobile = models.IntegerField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'contact_info'

    def __str__(self):
        return self.first_name+' '+self.last_name

class ContactMapInfo(models.Model):
    lattitude = models.CharField(max_length=1048)
    longitude = models.CharField(max_length=150)
    contact = models.ForeignKey(ContactInfo, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "contact_map_info"

    def __str__(self):
        return self.contact.first_name+' '+self.contact.last_name
