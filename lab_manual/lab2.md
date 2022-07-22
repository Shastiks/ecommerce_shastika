# Lab 2 Adding Brand, Category and Product


  ## a. Introduction:
  
  In our first lab, we made a produvt module. Presently, we include a brand, product and category within the product module which encompasses a structure of the er graph as appeared underneath:
  ![Screenshot1](https://github.com/BabeenDangol/Ecommerce_BabinDangol/blob/main/lab_manual/images/ER-product_module.png?raw%3Dtrue)
  
   ## b.Objective: 
 
        1.To Add Product, Brand, Category and Color
        2.To perform CRUD operations on all three models.  
        3.To verify the frontend and backend in the browser. 
        4.To get more information about the admin.py, models.py as well as other files that django framework provides
        5.To get more information about adding models and how models.py works

  ## c. Procedure:

**1. Adding the model Brand in the models.py**

  We downloaded the software and environments required for the project. Those were:

    class Category(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField()
    class Meta:
    verbose_name_plural = "Categories"

**2. Adding the model Product in the models.py**

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
      
      
 **3. Making changes to the db by performing migrations** 
 
    python manage.py makemigrations
    python manage.py migrate
              
  **4. Adding the following code to admin.py for enabling CRUD operations in the admin site**

    from .models import Brand, Category, Product
    admin.site.register(Brand)
    admin.site.register(Category)
    admin.site.register(Product)
  **5. Finally, running the project and performing CRUD operations on Brand, Category and Product**

    python manage.py runserver

    

  ## d. Output
  
  **1. Adding the models Brand, Category and Product**

  ![Screenshot1](https://github.com/BabeenDangol/Ecommerce_BabinDangol/blob/main/lab_manual/images/Screenshot%202022-06-12%20190129.jpg?raw%3Dtrue)
  
  
 **2. Brand Model**
 
   ![Screenshot2](https://github.com/BabeenDangol/Ecommerce_BabinDangol/blob/main/lab_manual/images/Screenshot%202022-06-12%20190201.jpg)

   ![ss3](https://github.com/BabeenDangol/Ecommerce_BabinDangol/blob/main/lab_manual/images/Screenshot%202022-06-12%20190219.jpg)

  **3. Category model**

   ![ss4](https://github.com/BabeenDangol/Ecommerce_BabinDangol/blob/main/lab_manual/images/Screenshot%202022-06-12%20190237.jpg?raw%3Dtrue)

   ![ss5](https://github.com/BabeenDangol/Ecommerce_BabinDangol/blob/main/lab_manual/images/Screenshot%202022-06-12%20190248.jpg?raw%3Dtrue)

 **4. Product model**

   ![ss6](https://github.com/BabeenDangol/Ecommerce_BabinDangol/blob/main/lab_manual/images/Screenshot%202022-06-12%20190306.jpg)
   
   ![ss7](https://github.com/BabeenDangol/Ecommerce_BabinDangol/blob/main/lab_manual/images/Screenshot%202022-06-12%20190321.jpg)

  ## e. Conclusion:

   As a result, in the second lab, we created the darnd,category and producl models.They are realated to each other through one eo many relationship.We have also used different data types provided by django.