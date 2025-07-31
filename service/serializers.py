from django.conf import settings
from rest_framework import serializers
from .models import OurServicesModel, OurTechnologyModel



class NestedTablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurServicesModel
        fields = ['title2', 'name2', 'description', 'icon']


class OurServicesSerializer(serializers.ModelSerializer):
    tables = serializers.SerializerMethodField()

    def get_tables(self, obj):
        return  obj.safe_translation_getter('tables', any_language=True)

    class Meta:
        model = OurServicesModel
        fields = ['id', 'title', 'name', 'tables']

    def get_tables(self, obj):
        request = self.context.get('request')
        tables = OurServicesModel.objects.all()
        return NestedTablesSerializer(tables, many=True, context={'request': request}).data





class NestedTechnologysSerializers(serializers.ModelSerializer):
    class Meta:
        model = OurTechnologyModel
        fields = ['name', 'icon']


class OurTechnologySerializer(serializers.ModelSerializer):
    technologys = serializers.SerializerMethodField()

    def get_technology(self, obj):
        return obj.safe_trabslation_getter('technologys', any_language=True)

    class Meta:
        model = OurTechnologyModel
        fields = ['id', 'title', 'technologys']

    def get_technologys(self, obj):
        request = self.context.get('request')
        technologys = OurTechnologyModel.objects.all()
        return NestedTechnologysSerializers(technologys, many=True, context={'request': request}).data








