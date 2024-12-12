from celery import shared_task
from .models import Candidate


@shared_task
def increment_votes(user_id: int, value: int):
    candidate = Candidate.objects.get(user_id=user_id)
    candidate.votes += value
    candidate.save()