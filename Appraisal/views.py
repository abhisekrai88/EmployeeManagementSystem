from rest_framework import generics
from .models import Appraisal
from .serializers import AppraisalSerializer

# Create your views here.

class AppraisalAPIView(generics.ListCreateAPIView):
    queryset = Appraisal.objects.all()
    serializers = [AppraisalSerializer]
