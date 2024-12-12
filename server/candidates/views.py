from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .models import Candidate
from .serializers import CandidateSerializer
from .tasks import increment_votes


class CandidateViewSet(CreateModelMixin, 
                       RetrieveModelMixin, 
                       GenericViewSet):
    
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    authentication_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=["patch"])
    def vote(self, request, pk=None):
        candidate = self.get_object()
        increment_votes.delay(candidate.user_id, 1)
        return Response("vote_success")