from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db import transaction
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Candidate
from .serializers import CandidateSerializer


@receiver(post_save, sender=Candidate)
@receiver(post_delete, sender=Candidate)
def send_candidate_update(sender, instance, **kwargs):
    def send_update():
        channel_layer = get_channel_layer()
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        async_to_sync(channel_layer.group_send)(
            "candidates",
            {
                "type": "candidate_update",
                "data": serializer.data,
            }
        )

    transaction.on_commit(send_update)
