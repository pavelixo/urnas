from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Candidate
from .serializers import CandidateSerializer


class CandidateConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("candidates", self.channel_name)

        try:
            candidates = await self.get_all_candidates()
            serializer_data = await database_sync_to_async(self.serialize_candidates)(candidates)
            await self.send_json(serializer_data)
        except Exception as e:
            await self.send_json({"error": f"Failed to load candidates: {str(e)}"})

    async def disconnect(self, code):
        await self.channel_layer.group_discard("candidates", self.channel_name)

    async def candidate_update(self, event):
        try:
            candidates = await self.get_all_candidates()
            serializer_data = await database_sync_to_async(self.serialize_candidates)(candidates)
            await self.send_json(serializer_data)
        except Exception as e:
            await self.send_json({"error": f"Failed to update candidates: {str(e)}"})

    @database_sync_to_async
    def get_all_candidates(self):
        return list(Candidate.objects.all().order_by("username"))

    def serialize_candidates(self, candidates):
        serializer = CandidateSerializer(candidates, many=True)
        return serializer.data
