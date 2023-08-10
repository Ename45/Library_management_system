from rest_framework import serializers

from books.models import Book, Author, Review


#
# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     isbn = serializers.CharField(max_length=13)
#     genre = serializers.CharField(max_length=8)
#

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'genre', 'copies', 'author']

    # author = AuthorSerializer()

    author = serializers.HyperlinkedRelatedField(
        queryset=Author.objects.all(),
        view_name="author-detail"
    )


class CreateBooKSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'genre', 'copies_bought', 'author']


# class AuthorSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=300)
#     last_name = serializers.CharField(max_length=300)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'firstName', 'lastName']


class CreateAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email']


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['id', 'name', 'description']

    def create(self, validated_data):
        return Review.objects.create(book_id=self.context['book_id'], **validated_data)
