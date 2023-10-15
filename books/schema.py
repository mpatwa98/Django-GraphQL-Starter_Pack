import graphene
from graphene_django import DjangoObjectType
from .models import Book


class BooksType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("id", "title", "excerpt")


class Query(graphene.ObjectType):
    allBooks = graphene.List(BooksType)

    def resolve_allBooks(root, info):
        return Book.objects.all()


schema = graphene.Schema(query=Query)
