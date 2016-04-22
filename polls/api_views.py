from rest_framework import generics
from models import Poll, Thread, PollSubject
from serializers import PollSerializer, VoteSerializer

class PollViewSet(generics.ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
