from django.shortcuts import render, redirect, get_object_or_404
from .models import Borrow, Product
from django.db.models import Q
def products(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        book_id = request.POST.get('book_id')
        category = request.POST.get('category')
        author = request.POST.get('author')
        description = request.POST.get('description')
        
        if name and book_id:
            data = Product(
                name=name,
                book_id=book_id,
                category=category,
                author=author,
                description=description
            )
            data.save()
            return redirect('products') 

    context = {
        'pro': Product.objects.all() 
    }
    return render(request, 'products/products.html', context)

def product(request):
    return render(request, 'products/product.html')

def delete_product(request):
    if request.method == 'POST':
        input_id = request.POST.get('book_id')
        
        book = get_object_or_404(Product, book_id=input_id)
        
        book.delete()
        
        return redirect('products')
    
    return render(request, 'products/delete.html')

# def delete2(request, book_id):
#     if request.method == 'POST':
#         input_id = request.POST.get('book_id')
        
#         book = get_object_or_404(Product, book_id=input_id)
        
#         book.delete()
        
#         return redirect('products')
    
#     return render(request, 'products/delete2.html')

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        book_id = request.POST.get('book_id')
        category = request.POST.get('category')
        author = request.POST.get('author')
        description = request.POST.get('description')
        
        if name and book_id:
            Product(
                name=name,
                book_id=book_id,
                category=category,
                author=author,
                description=description
            ).save()
            return redirect('products')
    
    return render(request, 'products/add.html')
def SearchForBooks(request):
    results = []
    toSearch = ""

    if request.method == "POST":
        toSearch = request.POST.get('toSearch')

        if toSearch:
            results = Product.objects.filter(
    Q(name__icontains=toSearch) | 
    Q(author__icontains=toSearch) | 
    Q(category__icontains=toSearch)
).distinct()

    return render(request, 'products/Search.html', {'results': results, 'toSearch': toSearch})


def product2(request, book_id):
    book =Product.objects.get(id=book_id)
    return render(request, 'products/products2/product2.html', {'book': book})

def products2(request):
    return render(request, 'products/products2/products2.html', {'pro': Product.objects.all()})

def BorrowedBooks(request, book_id):
    book = Product.objects.get(id=book_id)
    if request.method == 'POST':
        user_name = request.POST.get('borrowerName')
        user_id = request.POST.get('borrowerId')
        return_date = request.POST.get('returnDate')
        Borrow(
            user_name=user_name,
            user_id=user_id,
            book_id=book_id,
            return_date=return_date,
        ).save()
        book.borrowed = True
        book.save()
        return redirect('displayBooks')
    return render(request, 'products/Borrow a Book.html', {'book': book})

def displayBooks(request):
    context = {'books': Borrow.objects.all()}
    return render(request, 'products/BorrowedBooks.html', context)

def borrow(request, book_id):
    book = Product.objects.get(id=book_id)
    return render(request, 'products/Borrow a Book.html', {'book': book})


def edit(request, book_id):
    book = Product.objects.get(id=book_id)
    if request.method == 'POST':
        book.name = request.POST.get('title')
        book.book_id = request.POST.get('book_id')
        book.category = request.POST.get('category')
        book.author = request.POST.get('author')
        book.format = request.POST.get('format')
        book.language = request.POST.get('language')
        book.save()
        return redirect('products')  
    return render(request, 'products/Edit books details.html', {'book': book})  


def Books(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        book_id = request.POST.get('book_id')
        category = request.POST.get('category')
        author = request.POST.get('author')
        description = request.POST.get('description')
        
        if name and book_id:
            data = Product(
                name=name,
                book_id=book_id,
                category=category,
                author=author,
                description=description
            )
            data.save()
           
            return redirect('Books') 

    context = {
        'books': Product.objects.all() 
    }
   
    return render(request, 'products/Books.html', context)

def displayBooks(request):
    return render(request, 'products/Books.html')