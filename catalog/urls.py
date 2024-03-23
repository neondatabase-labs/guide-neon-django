from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.list_authors, name='list_authors'),
    path('books/<int:author_id>/', views.list_books_by_author, name='list_books_by_author'),
]
