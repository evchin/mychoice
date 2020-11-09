from rest_framework import serializers
from .models import User, Election, Candidate, Position

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'

class PositionSerializer(serializers.ModelSerializer):
    candidate_set = CandidateSerializer(many=True, read_only=True)

    class Meta:
        model = Position
        fields = '__all__'

class ElectionSerializer(serializers.ModelSerializer):
    position_set = PositionSerializer(many=True, read_only=True)

    class Meta:
        model = Election
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'