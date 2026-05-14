from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'), 
    path('search', views.SearchForBooks, name='SearchForBooks'),
    path('product/<int:book_id>/', views.product, name='product'),
    path('delete/', views.delete_product, name='delete_product'),
    path('add/', views.add_product, name='add_product'),
    path('products2/', views.products2, name='products2'),
    path('product2/<int:book_id>/', views.product2, name='product2'),
    path('borrow/<int:book_id>/', views.borrow, name='borrow'),
    path('displayBooks/', views.displayBooks, name='displayBooks'),
    path('borrowed/<int:book_id>/', views.BorrowedBooks, name='BorrowedBooks'),  
    path('edit/<int:book_id>/', views.edit, name='edit'),
    # path('delete2/<int:book_id>/', views.delete2, name='delete2'),
     path('Books/', views.Books, name='Books'), 
]