from django.db import models

# Create your models here.
class BookStoreModel(models.Model):
    CATEGORY = (
        ('Mystery', 'Mystrey'),
        ('Thriller', 'Thriller'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Humor','Humor'),
        ('Horror','Horror'),
    )
    id =  models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    category = models.CharField(max_length=30, choices=CATEGORY)
    first_pub = models.DateTimeField(auto_now_add=True)  #auto_now_add=True eita dile 1st time 1 bar auto add hoye jabe
    last_pub = models.DateTimeField(auto_now=True)  #auto_now=True eita dile auto add hobe but edit korar sathe sathe time change hobe
    
    
# Module inheritance
# 1. abstract base class
# 2. multitable inheritance
# 3. proxy model

# 1. abstract base class: sob gulo object class abstract class niye toiri hobe kintu abstract class er kono object toiri hobe na
