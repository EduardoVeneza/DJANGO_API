from rest_framework import serializers
from trilhas.models import Trail, Link, Step, Attachment

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


class StepSerializer(serializers.ModelSerializer):
    # Para facilitar a leitura dos links e attachments relacionados, adiciono nested serializers (read-only)
    links = serializers.SerializerMethodField()
    attachments = serializers.SerializerMethodField()

    class Meta:
        model = Step
        fields = ['id', 
                  'title', 
                  'description', 
                  'video_url', 
                  'watched', 
                  'trail', 
                  'position', 
                  'links', 
                  'attachments'
                  ]
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

    def get_links(self, obj):
        links = obj.links.all()
        return LinkSerializer(links, many=True).data

    def get_attachments(self, obj):
        attachments = obj.attachments.all()
        return AttachmentSerializer(attachments, many=True).data


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 
                  'link', 
                  'description', 
                  'created_at', 
                  'step'
                  ]


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 
                  'name', 
                  'phone', 
                  'email', 
                  'video_duration', 
                  'file_url', 
                  'created_at', 
                  'step'
                  ]
