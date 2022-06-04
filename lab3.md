# Lab 3

## Objective
To add search field for product brands and categories.

## Introduction
A website can only be interactive if it provides the users with their desired thought. Here, we are goint to add search fields for the products, brands and categories and also added a feature where we can see the images of the products.

## Procedure
First we rplaced the code for **admin.site.register(Product)** with 
    
    class ProductAdmin(admin.ModelAdmin):
      list_display = ["name", "price", "brand", "category",]
      search_fields = ["name", "price", "brand__name", "category__name",]
      list_filter = ["brand","category",]
      readonly_fields = ["quantity",]
 
    class Meta:
      model = Product
    admin.site.register(Product, ProductAdmin)
then **admin.site.register(Category)** with 

    class Meta:
        model = Category
    admin.site.register(Category, CategoryAdmin)
    class ProductAdmin(admin.ModelAdmin):
    list_display = ["image_tag", "name", "price", "brand", "category",]
    search_fields = ["name", "price", "brand__name", "category__name",]
    list_filter = ["brand","category","price",]
    
and **admin.site.register(Brand)** with 
  
    class Meta:
        model = Brand
    admin.site.register(Brand, BrandAdmin)
    class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "is_active",]
    search_fields = ["name", "is_active",]
    
 We than ran the server using **python manage.py runserver** and edited the code for products in _models.py_ by adding the image tag and also marked it safe :
 
      class Product(models.Model):
      name = models.CharField(max_length=200)
      price = models.FloatField()
      quantity = models.IntegerField()
      image_url = models.CharField(max_length=500)
      color_code = models.CharField(max_length=20)
      brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
      category = models.ForeignKey(Category, on_delete=models.CASCADE)
      registered_on = models.DateTimeField()
      is_active = models.BooleanField()
      def image_tag(self):
    return mark_safe(f'<img src="{self.image_url}" width="50" height="50" />')
    image_tag.short_description = "Product"
    def __str__(self):
    return self.name
    
## Outputs
1.Search bar for product

![image](https://user-images.githubusercontent.com/81128122/171986906-77b8cb83-bb24-4bdc-8c6c-82ca2346e214.png)

2.Search bar for brand
![image](https://user-images.githubusercontent.com/81128122/171986931-7f2d5200-e1fb-436c-9bc3-6f6de4881a29.png)


3.Search bar for category
![image](https://user-images.githubusercontent.com/81128122/171986945-1704bac1-1346-44d7-a8c6-7dee911ee72d.png)


4.images of the product

![image](https://user-images.githubusercontent.com/81128122/171986970-53b3903b-d179-4ce1-9125-6a82cc52d957.png)


## Concluison
Therefore, in this lab we used different codes to  create search bar for product, brands, and categories and also displayed the images for the products in the site.
