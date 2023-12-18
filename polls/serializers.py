from rest_framework import serializers

from .models import Question
import json

class QuestionSerializer(serializers.ModelSerializer):
    #user=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Question
        fields = '__all__'