from django.db import models

# Create your models here.

# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     bio = models.TextField()
#
#     def __str__(self):
#         return self.name
#
# class Book(models.Model):
#     GENRE_CHOICES = [
#         ('FIC', 'Fiction'),
#         ('NON', 'Non-fiction'),
#         ('SCI', 'Science Fiction'),
#         ('FAN', 'Fantasy'),
#         ('MYS', 'Mystery'),
#         ('THR', 'Thriller'),
#         ('ROM', 'Romance'),
#         ('HIS', 'Historical'),
#     ]
#
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
#     publication_date = models.DateField()
#     genre = models.CharField(
#         max_length=3,
#         choices=GENRE_CHOICES,
#         default='FIC',
#     )
#
#     def __str__(self):
#         return self.title
#
# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#
#     def __str__(self):
#         return self.name
#
# class Course(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     students = models.ManyToManyField(Student, related_name='courses')
#
#     def __str__(self):
#         return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)