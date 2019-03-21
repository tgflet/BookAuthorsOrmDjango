from django.shortcuts import render, redirect, HttpResponse
from .models import Book, Author

# Create your views here.
def index(request):
    context={
        "all_books": Book.objects.all()
    }
    return render(request, 'index.html',context)
def authors(request):
    context={
        "all_authors": Author.objects.all()
    }
    return render(request, 'index2.html', context)
def add_book(request):
    Book.objects.create(title=request.POST['title'],desc=request.POST['desc'])

    return redirect('/')

def add_author(request):
    Author.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],notes=request.POST['desc'])
    return redirect('/authors')
def author_info(request,num):
    number=int(num)
    author=Author.objects.get(id=number)
    curated=Book.objects.exclude(authors=author)
    context={
        "select_author" : author,
        "book": author.books.all().values("title"),
        "all_authors": Author.objects.all(),
        "all_books":curated,
    }
    return render(request,"author.html",context)

def book_info(request, num):
    number=int(num)
    book= Book.objects.get(id=number)
    curated=Author.objects.exclude(books=book)
    context={
        "select_book" : book,
        "authors": book.authors.all().values("first_name","last_name"),
        "all_authors": curated,
    }
    return render(request, 'book.html', context)
def join(request):
    x=request.POST['source']
    source=Book.objects.get(id=request.POST['source'])
    new=Author.objects.get(id=request.POST['new'])
    source.authors.add(new)
    return redirect('/books/'+x)

def connect(request):
    x=request.POST['source']
    source=Author.objects.get(id=request.POST['source'])
    new=Book.objects.get(id=request.POST['new'])
    source.books.add(new)
    return redirect('/authors/'+x)

def catchall(request):
    print(request)
    return HttpResponse("opps")