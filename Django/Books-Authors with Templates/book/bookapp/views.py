from django.shortcuts import render, redirect
from bookapp.models import Book, Author

def index(request):
    context ={
        "books" : Book.objects.all()
    }
    return render(request, "index.html", context)
def process_add(request):
    if (request.POST['which_form'] == "add_book"):
        Book.objects.create(title = request.POST['book_title'], desc = request.POST['book_desc'])
    if (request.POST['which_form'] == "add_author"):
        Author.objects.create(first_name= request.POST['first_name'], last_name = request.POST['last_name'], notes = request.POST['notes'])        
    return redirect('/')
def books(request, book_id):
    book = Book.objects.get(id = book_id)
    context = {
        "selected_book" : book,
        "all_authors" : Author.objects.exclude(books = book) 
    }
    return render(request, "book.html", context)
def view_author(request, auth_id):
    author = Author.objects.get(id = auth_id)
    context = {
        "selected_author" : author,
        "all_books" : Book.objects.all()    
    }
    return render(request, "author.html", context)

def authors(request):
    context = {
        "all_authors" : Author.objects.all(),
        
    }
    return render(request, "author2.html", context)
def add_author(request, id):
    if (request.POST['which_form'] == "add_author"):
        Book.objects.get(id = id).authors.add(Author.objects.get(id = request.POST['author_selected']))   
    if (request.POST['which_form'] == "add_book"):
        Author.objects.get(id = id).books.add(Book.objects.get(id = request.POST['book_selected']))   
    return redirect('/')


