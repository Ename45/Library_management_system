from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .serializer import BookSerializer, AuthorSerializer, CreateAuthorSerializer, CreateBooKSerializer, ReviewSerializer
from .models import Author, Book, Review

# Create your views here.

users = [
    {"name": "sheriff"},
    {"name": "Ned"},
    {"name": "sher"},
]


# when you have related code in two different view, use ModelViewSet
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = CreateBooKSerializer

    def get_serializer_context(self):
        return {'request': self.request}


# class BookList(ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = CreateBooKSerializer
#
#     def get_serializer_context(self):
#         return {'request': self.request}
#
#
# class BookDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     def get_serializer_context(self):
#         return {'request': self.request}


# when you have related code in two different view, use ModelViewSet
class AuthorViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = CreateBooKSerializer


# class AuthorList(ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#
#
# class AuthorDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer


class ReviewViewSet(ModelViewSet):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(book_id=self.kwargs['book_pk'])

    def get_serializer_context(self):
        return {'book_id': self.kwargs['book_pk']}
