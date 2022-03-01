from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.id}: {self.name}'

    class Meta:
        verbose_name_plural = 'people'


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id}: {self.name}'

    class Meta:
        verbose_name_plural = 'categories'


class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
    person_responsible = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    category = models.ManyToManyField(Category)
