from django.contrib import admin


from .models import Books, Category, Author 

admin.site.register(Books)
admin.site.register(Category)
admin.site.register(Author)
