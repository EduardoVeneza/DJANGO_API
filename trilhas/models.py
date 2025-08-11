from django.db import models

# Create your models here.
class Trail(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    number_of_steps = models.PositiveSmallIntegerField(default=1)
    autor = models.CharField(max_length=255, default='')

class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_url = models.URLField(max_length=200, default='', blank=True)
    watched = models.BooleanField(default=False)
    trail = models.ForeignKey(Trail, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    position = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('trail', 'position') # Garante que a position seja unico somente na respectiva trilha

class Link(models.Model):
    link = models.URLField(max_length=200)
    description = models.TextField(max_length=1024, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    step = models.ForeignKey(Step, related_name="links", on_delete=models.CASCADE)

    def __str__(self):
        return self.link


class Attachment(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    video_duration = models.DurationField(blank=True, null=True)  # timedelta
    file_url = models.URLField(max_length=500, blank=True, null=True)  # caso seja arquivo remoto
    created_at = models.DateTimeField(auto_now_add=True)
    step = models.ForeignKey(Step, related_name="attachments", on_delete=models.CASCADE)

    def __str__(self):
        return self.name if self.name else f"Attachment #{self.id}"