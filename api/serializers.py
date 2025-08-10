from rest_framework import serializers
from trilhas.models import Trail, Link, Step

class TrailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trail
        fields = '__all__'

    def validate_title(self, value):
        # value = título enviado no POST
        if Trail.objects.filter(title=value).exists():
            raise serializers.ValidationError("Já existe um trail com esse título.")
        return value


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