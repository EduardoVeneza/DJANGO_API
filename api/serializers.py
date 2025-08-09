from rest_framework import serializers
from trilhas.models import Trail, Link, Step

class TrailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trail
        fields = '__all__'


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = [
            
        ]


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = [
            
        ]