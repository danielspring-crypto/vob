from django.shortcuts import render, get_object_or_404
from .models import Category, Book

def index(request):
	return render(request, 'book/index.html')

def book_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	books = Book.objects.filter(available=True)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		books = books.filter(category=category)
	return render(request, 'book/list.html', {'category':category, 'categories':categories, 'books':books})



def book_detail(request, id, slug):
	book = get_object_or_404(Book, id=id, slug=slug, available=True)
	return render(request, 'book/detail.html', {'book':book})
