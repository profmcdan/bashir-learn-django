from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class TodoSerializerOne(serializers.Serializer):
    title = serializers.CharField()
    date_time = serializers.DateTimeField()

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # instance.title = validated_data.get('title', instance.title)
        # instance.date_time = validated_data.get('date_time', instance.date_time)
        # instance.save()
        # return instance
        return Todo.objects.update(instance, validated_data)
