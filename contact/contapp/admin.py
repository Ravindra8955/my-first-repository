from django.contrib import admin
from django.contrib.auth.models import User, Group
from contapp.models.product import Category, Product, ProductImage, ContactInfo, ContactMapInfo
from django.utils.html import format_html

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_on', 'updated_on')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines= [ProductImageAdmin]
    list_display = ('product_name','product_description','image_tag','created_on', 'updated_on')

    # def render_change_form(self, request, context, *args, **kwargs):
    #     #here we define a custom template
    #     self.change_form_template = 'contapp/change_form_template.html'
    #     extra = {
    #         "help_text" : "To delete multiple image select the checkbox and do save"
    #     }
    #     context.update(extra)
    #     return super(ProductAdmin, self).render_change_form(request, context, *args, **kwargs)

    def image_tag(self, obj):
        return format_html('<img src="{0}" style="width: 45px; height:45px;" />'.format(obj.product_image.url))

@admin.register(ContactInfo)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('mobile','first_name','last_name','city','created_on', 'updated_on')

@admin.register(ContactMapInfo)
class MapAdmin(admin.ModelAdmin):
    list_display = ('contact', 'lattitude','longitude', 'created_on','updated_on')


admin.site.unregister(User)
admin.site.unregister(Group)
