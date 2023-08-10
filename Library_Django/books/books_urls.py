from django.urls import path, include
from rest_framework_nested import routers

from . import views

# we use router to work only with viewset in our view
# router = SimpleRouter()
#         OR
router = routers.DefaultRouter()
router.register('books', views.BookViewSet)
router.register('authors', views.AuthorViewSet)
router.register('reviews', views.ReviewViewSet, basename='reviews')

books_router = routers.NestedDefaultRouter(router, 'books', lookup='book')
books_router.register('reviews', views.ReviewViewSet, basename='book-reviews')

# urlpatterns = [
#     path('', include(router.urls))
# ]

# OR
urlpatterns = router.urls + books_router.urls
