from django.db import models

# Create your models here.
class Trail(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    create_at = models.DateField(auto_now_add=True)
    number_of_steps = models.PositiveSmallIntegerField()
    # Autor?

class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    watched = models.BooleanField(default=False)
    trail = models.ForeignKey(Trail, on_delete=models.CASCADE)
    position = models.PositiveSmallIntegerField(unique=True)

    class Meta:
        unique_together = ('trail', 'position') # Garante que a position seja unico somente na respectiva trilha

class Link(models.Model):
    link = models.URLField(max_length=200)
    create_at = models.DateField(auto_now_add=True)
    step = models.ForeignKey(Step, on_delete=models.CASCADE)

# class Connection(models.Model):
#     pass