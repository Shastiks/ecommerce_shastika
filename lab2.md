# Lab 2 
## Objective: To add products,brands and categories.

Introduction:
For an e-commerce website, the proper identification of products and their respective brands and categories are very important. An ER diagram helps us analyze the er model to enhance our product_module.
![image](https://user-images.githubusercontent.com/81128122/171983621-0110aebb-34ed-496a-9996-9584a2794a96.png)

## Procedure:
A.In the product_module, We opened the  “models.py” and edited code for:

1.Brand model as follows:

	class Brand(models.Model):
 		name = models.CharField(max_length=200)
 		is_active = models.BooleanField()
 
2.Category model as follows:

	class Category(models.Model):
 		name = models.CharField(max_length=200)
		is_active = models.BooleanField()
		
		
3.Product model as follows:

	class Product(models.Model):
 		name = models.CharField(max_length=200)
 		price = models.FloatField()
 		quantity = models.IntegerField()
 		color_code = models.CharField(max_length=20)
 		brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
 		category = models.ForeignKey(Category, on_delete=models.CASCADE)
 		registered_on = models.DateTimeField()
 		is_active = models.BooleanField()

After this we used the following codes to make the changes to our server 
	
	python manage.py makemigrations
	python manage.py migrate
	
Then we used the following codes in admin.py to pefrom the curd operations.

		from .models import Brand, Category, Product
		admin.site.register(Brand)
		admin.site.register(Category)
		admin.site.register(Product)
  
	
Lastly we used to the following operations to run the server and analyze our outputs.

	python manage.py runserver


## Outputs 
1.Insertion of product brand and category
![image](https://user-images.githubusercontent.com/81128122/171986017-551d6ad3-29c9-4f71-916f-815d6b8b8072.png)



2.CURD operations on brand category and products

![image](https://user-images.githubusercontent.com/81128122/171986203-8e9fba86-0123-4dc2-862d-3721b9ea6722.png)


## Conclusion
Hence, in this lab we learnt how to add product modules and peform curd operations on them.
	
