from rest_framework import serializers
from trilhas.models import Trail, Link, Step

class TrailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trail
        fields = '__all__'

    def validate_title(self, value):
        qs = Trail.objects.filter(title=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
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
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Step.objects.all(),
                fields=['trail', 'position'],
                message="Já existe um step com essa posição nessa trilha."
            )
        ]
        # read_only_fields = ['trail']

    def validate_position(self, value):
        if value <= 0:
            raise serializers.ValidationError("A posição deve ser maior que zero.")
        return value