from django.shortcuts import render
from .models import Author, Genre, Book, BookInstance
# Create your views here.

# creamos la funcion index


def index(request):
    # En el modelo Book obtiene los datos que son los objectos(objects)
    # all() --> obtiene todos los datos
    # count() --> cuenta todos los datos
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_authors = Author.objects.all().count()

    # Aqui se trabaja con la base de datos
    # Cuales son los libros disponibles - Avaliable ('a')
    # status__exact --> es que quiero que tenga un campo estado, cuyo estado se exactamente a la letra 'a'
    # y se pone el count para que me de el numero de elementos
    disponibles = BookInstance.objects.filter(status__exact='a').count()

    # Estoy se llama preparar el contexto, quiere decir cuando se dispara la funcion index y toda esta funcion se mostrara dentro de index.html y va a poder usar unos ciertos datos
    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_authors': num_authors,
            'num_instances': num_instances,
            'disponibles': disponibles,
        }
    )
