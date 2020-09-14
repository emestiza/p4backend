from rest_framework import serializers
from api.models import Subject, Topic


# referenced relationship should be above subject class or else relationship won't be recognized
class TopicSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')

    class Meta:
        model = Topic
        fields = ('id', 'name', 'owner', 'subject', 'description', 'created_at', 'updated_at', 'is_public')


class SubjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')  # owner's name is read only, can't write over
    topic = TopicSerializer(many = True, read_only = True, required = False)

    class Meta:
        model = Subject
        fields = ('id', 'name', 'owner', 'topic', 'description','created_at', 'updated_at')

