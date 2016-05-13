from rest_framework import serializers
from .models import Jrello


class JrelloSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Jrello
        fields = ('id', 'title', 'description', 'is_completed', 'priority', 'last_edited', 'url')
