# Django GraphQL Project README

This README.md file provides instructions for setting up a Django project with GraphQL using the provided code snippets.

## Prerequisites

Before starting, ensure you have the following installed on your system:

- Python 3
- Pip (Python package manager)

## Project Setup

1.  **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    ```

2.  **Activate the virtual environment:**

    ```bash
    source venv/bin/activate
    ```

3.  **Install Django:**

    ```bash
    pip install django
    ```

4.  **Install GraphQL support using Graphene-Django:**

    ```bash
    pip install graphene-django
    ```

5.  **Create a new Django project and an app:**

    ```bash
    django-admin startproject core .
    python3 manage.py startapp books
    ```

6.  **Add the 'books' and 'graphene_django' app to `INSTALLED_APPS` in `core/settings.py`**:

    ```python
    # core/settings.py
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'graphene_django', # Add 'graphene_django' here
        'books',  # Add 'books' here
    ]
    ```

7.  **Define a model in `books/models.py`**:

    ```python
    # books/models.py
    from django.db import models

    class Book(models.Model):
        title = models.CharField(max_length=100)
        excerpt = models.TextField()

        def __str__(self):
            return self.title
    ```

8.  **Create database tables and apply migrations:**

    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

9.  **Create a GraphQL schema file:**

    ```bash
    touch books/schema.py
    ```

10. **Populate `books/schema.py` with GraphQL schema definitions:**

    ```python
    # books/schema.py
    import graphene
    from graphene_django import DjangoObjectType
    from .models import Book

    class BookType(DjangoObjectType):
        class Meta:
            model = Book
            fields = ("id", "title", "excerpt")

    class Query(graphene.ObjectType):
        allBooks = graphene.List(BookType)

        def resolve_allBooks(root, info):
            return Book.objects.all()

    schema = graphene.Schema(query=Query)
    ```

11. **Update `core/urls.py` to include the Books endpoint:**

    ```python
    # core/urls.py
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls'))
    ]
    ```

12. **Update `books/urls.py` to include the GraphQL endpoint:**

    ```python
    # core/urls.py
    from django.urls import path
    from graphene_django.views import GraphQLView
    from books.schema import schema

    urlpatterns = [
        # ...
        path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
    ]
    ```

13. **Register the `Book` model in `core/admin.py`:**

    ```python
    # core/admin.py
    from django.contrib import admin
    from books.models import Book

    admin.site.register(Book)
    ```

14. **Create a superuser for the admin interface:**

    ```bash
    python3 manage.py createsuperuser
    ```

15. **Visit `http://localhost:8000/admin` in your browser and log in with the superuser credentials you created.**

16. **Add few books from the admin interface:**

17. **Start the development server once more:**

    ```bash
    python3 manage.py runserver
    ```

18. **Visit `http://localhost:8000/graphql` and play with queries**

Now, you have set up a Django project with GraphQL support. You can use the GraphQL endpoint at `http://localhost:8000/graphql` to interact with your data. The `Book` model is available in the admin interface for data management.
