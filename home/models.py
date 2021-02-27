from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    desc = models.TextField()
    date = models.DateField()

    #to view name instead of "contact object" in admin
    def __str__(self):
        return self.name
    

#makemigrations - create changes and store in a file
#migrate - apply the pending changes created by makemigrations
