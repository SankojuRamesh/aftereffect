# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import ProjectsModel,CompositsModel, LayersModel
import logging
from django_filters import rest_framework as filters
from  rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema

class ForceDeleteSerializer(serializers.Serializer):
    force_delete = serializers.BooleanField(default=False)

@swagger_auto_schema(request_body=ForceDeleteSerializer)
def destroy(self, request, *args, **kwargs):
    ...
class ProjectsFilter(filters.FilterSet):
    class Meta:
        model =ProjectsModel
        fields ='__all__'



class compositFilter(filters.FilterSet):
    class Meta:
        model =CompositsModel
        fields ='__all__'



class layerFilter(filters.FilterSet):
    class Meta:
        model =LayersModel
        fields =['layer_name', "composit", 'layer_type']
 