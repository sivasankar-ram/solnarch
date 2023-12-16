#from django.shortcuts import render
#from django.template import loader
# Create your views here.
#from django.http import HttpResponse
from unittest import result
from .models import Question
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import QuestionSerializer
from django.http import JsonResponse
from datetime import datetime

@api_view(['GET'])
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    results = QuestionSerializer(latest_question_list, many=True)
    return JsonResponse(results.data, safe=False)    

@api_view(['POST'])
def addPoll(request):
    request.data['pub_date']=datetime.now()
    results = QuestionSerializer(data=request.data)
    if results.is_valid():
        results.save()
    else:
        print("ERROR")
    return Response(results.data)

@api_view(['DELETE'])
def deletePoll(request, pk):
    results = Question.objects.get(id=pk)
    results.delete()
  #  cache.set("keys", JsonResponse(results.data, safe=False), timeout=CACHE_TTL)
    return Response("The POLL is deleted successfully")