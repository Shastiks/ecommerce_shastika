# ecommerce_shastika
## Objective
To create frontend for the website
## Introduction
In this lab of E-commerce we continued the lab by adding _index.html_ and _base.html_ to enhance our e-commerce website.
## Procedure
 1. First we prepared template for Django and created a directory _templates_ and added a template for base file “base.html”.
 2. To make “templates/base.html”  globally available, we made following adjustment to _settings.py_
   
        TEMPLATES = [
        {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        
  3. We created a html file _index.html_ along with a directory _templates_ inside _product_module_
  4. We opened _views.py_ from the _product_module_ and added the code for search operation i.e. GET and POST .
  5. Then in  _product_module_ we created a file for _urls.py_ and added the URL routing config.
  
          from django.urls import path
          from .views import index
          urlpatterns = [
           path('', index),
          ]
  6. In *ecommerce_shastika > urls.py*, we included _product_module.urls_
  
            from django.contrib import admin
            from django.urls import path, include
            urlpatterns = [
             path('admin/', admin.site.urls),
             path('', include('product_module.urls')),
            ]
  7. Lastly we used the code _python manage.py runserver_ to run and generate outputs

## Outputs
![image](https://user-images.githubusercontent.com/81128122/175188375-6fdb890c-b183-4790-a34f-f90d8660dc65.png)
![image](https://user-images.githubusercontent.com/81128122/175188532-5d10d83a-5f6e-47af-b7d9-17aa5338a676.png)
![image](https://user-images.githubusercontent.com/81128122/175188629-30f03d8a-8167-421a-8046-630a8fa549b3.png)
![image](https://user-images.githubusercontent.com/81128122/175188724-f5d2d61c-df6b-42b9-9713-917bef170f79.png)
