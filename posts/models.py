from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField('título', max_length=200)
    image = models.ImageField(upload_to="images/")
    data = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    def __str__(self) -> str:
        return self.titulo + " - " + self.image.url
        #return self.titulo
