from django.db import models
from django.urls import reverse
import uuid
# Create your models here.


class Genre(models.Model):
    name = models.CharField(
        max_length=64, help_text="Pon el nombre del genero")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=32)

    # Esto es una referencia, la base de datos relacionales puede tener relaciones
    # el author no va estar escrito dentro de la class Book,
    # el ForeignKey en Django dice que un campo de esta tabla va a estar relacionado con otra tabla y los datos de este elemento tiene que extraerlos de otra tabla(clase).
    # on_delete=models.SET_NULL --> significa si se borra el autor dentro de la clase Book sera null, es decir enixitente
    # null=True --> significa que este campo author pueda tener el valor null
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    # TextField() es un campo de texto mas grande que un Charfield() que en si Charfield puede soportar 255 caracteres y los Texfield tiene una longitud ilimitada
    summary = models.TextField(
        max_length=100, help_text="Pon aqui de que va el libro")

    # Este es otra referencia
    isbn = models.CharField('ISBN', max_length=13,
                            help_text="El ISBN de 13 caracteres")

    # ManyToManyField() aqui significa que un Book(libro) puede ser de varios generos(Genre), ejm el Book puede ser de genero de suspenso y terror.
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    # UUIDField es un numero mucho mas largo ejm. 85b94505-c758-4975-923a-dd660b91f692
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Id unico para este libro")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    # Se crean estas variables para luego usarlas
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    # se crea una variable status, y esta variable lo asignamos con cualquira de LOAN_STATUS
    # max_length es para poner cualquiera de LOAN_STATUS como 'm', 'o', 'a' o 'r'
    # choices que son las opciones disponibles
    # blank=True se permite que no tengan datos o que este vacio
    # default=m  significa que este por defecto m
    status = models.CharField(max_length=1, choices=LOAN_STATUS,
                              blank=True, default='m', help_text="Disponibilidad del libro")

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return '%s (%s)' % (self.id, self.book.title)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)
