from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            "id",
            "title",
            "body",
            "created_at",
            "done_at",
            "updated_at",
            "deleted_at",
            "status",
        )
        read_only_fields = ('created_at', 'done_at', 'updated_at', 'deleted_at',)

class TestTodoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length = 100)
    body = serializers.CharField(max_length = 200)
    status = serializers.IntegerField()

    def validate_title(self, value):
        # Validación customizada
        if "$" in value:
            raise serializers.ValidationError("Error, el título no puede tener el símbolo de $")
        return value

    def validate_body(self, value):
        # Validación customizada
        if "$" in value:
            raise serializers.ValidationError("Error, el cuerpo no puede tener el símbolo de $")
        return value

    #agregar datos
    def create(self, validated_data):
        print(validated_data)
        return Todo.objects.create(**validated_data)