from django.urls import path 
from . import views



app_name = 'books'
urlpatterns = [
    path('list', views.BooksListView.as_view(), name='booklist'),
    path('detail/<int:pk>', views.BooksDetailView.as_view(), name='bookdetail'),
    path('bookadd', views.BooksAdd.as_view(), name='bookadd'),
    #path('category/<int:category_id>', views.CategoryBooksList, name='categorybookslist'),
    #path('author/<int:author_id>', views.AuthorDetail, name='authordetail'),
    #path('authoradd', views.AuthorAdd, name='authoradd'),
    #path('authoropus/<int:author_id>', view.AuthorOpusList, name='authoropuslist'),

]