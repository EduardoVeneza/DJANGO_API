from rest_framework import serializers
from trilhas.models import Trail, Link, Step

class TrailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trail
        fields = '__all__'

    def validate_title(self, value):
        # Para update, ignora o próprio registro
        trail_id = self.instance.id if self.instance else None
        if Trail.objects.filter(title=value).exclude(id=trail_id).exists():
            raise serializers.ValidationError("Já existe um trail com esse título.")
        return value


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = [
            
        ]


class StepSerializer(serializers.ModelSerializer):
    # trail = serializers.PrimaryKeyRelatedField(read_only=True)  # só leitura, vem da URL

    class Meta:
        model = Step
        fields = ['id', 'title', 'description', 'watched', 'trail', 'position']
        # read_only_fields = ['trail']
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Step.objects.all(),
                fields=['trail', 'position'],
                message="Já existe um step com essa posição nessa trilha."
            )
        ]

    def validate_position(self, value):
        if value <= 0:
            raise serializers.ValidationError("A posição deve ser maior que zero.")
        return value