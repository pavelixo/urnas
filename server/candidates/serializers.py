from rest_framework import serializers
from .models import Candidate


class CandidateSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Candidate
        fields = "__all__"
        extra_kwargs = {
            "votes": {"read_only": True},
        }
