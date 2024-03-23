from django.http import JsonResponse
from django.core import serializers
from .models import Author, Book

def list_authors(request):
    authors = Author.objects.all()
    data = [serializers.serialize('json', authors)]
    return JsonResponse(data, safe=False)

def list_books_by_author(request, author_id):
    books = Book.objects.filter(author_id=author_id)
    data = [serializers.serialize('json', books)]
    return JsonResponse(data, safe=False)
