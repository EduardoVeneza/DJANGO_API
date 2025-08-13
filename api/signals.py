from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Step

@receiver([post_save, post_delete], sender=Step)
def update_trail_step_count(sender, instance, **kwargs):
    instance.trail.update_step_count()