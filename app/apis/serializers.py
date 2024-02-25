from rest_framework import serializers
from ..model_builder import ModelBuilder

class ModelSerailizer (serializers.Serializer) : 
    app = serializers.CharField()
    model_name = serializers.CharField()
    has_uuid = serializers.BooleanField(default=False)
    fields = serializers.ListField()

    def generate_model (self) : 
        model = ModelBuilder(
            **self.validated_data
        )

        return model.generate()
