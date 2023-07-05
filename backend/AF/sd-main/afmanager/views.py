from django.shortcuts import render
from django.http import HttpResponse
# views.py
from rest_framework import viewsets, permissions, serializers
from django.views.decorators.csrf import csrf_exempt
from . import filter
import json
import requests
# Create your views here.
import re
import asyncio
 
from .models import LayersModel, CompositsModel, ProjectsModel



class ProjectSerializer(serializers.ModelSerializer):
     class Meta:
        model = ProjectsModel
        fields = '__all__'


class CompositSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompositsModel
        fields = '__all__'

 

class LayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LayersModel
        fields = '__all__'

 

class  ProjectViewset(viewsets.ModelViewSet):
    queryset = ProjectsModel.objects.all()
    filterset_class = filter.ProjectsFilter
    serializer_class = ProjectSerializer


     
class CompositViewSet(viewsets.ModelViewSet):
    queryset = CompositsModel.objects.all()
    filterset_class = filter.compositFilter
    serializer_class = CompositSerializer

    
class LayerViewSet(viewsets.ModelViewSet):
    queryset = LayersModel.objects.all()
    serializer_class = LayerSerializer
    filterset_class = filter.layerFilter
    # permission_classes = [permissions.IsAuthenticated]


def Home(request):   
    projects =  ProjectsModel.objects.all()
    return render(request, 'dashboard.html',  {'data':projects})



def Composits(request):
    comosits = CompositsModel.objects.all()
    pid = request.GET.get('project', False)
    if pid:
        comosits = comosits.filter(project=pid)
    return render(request, 'composits.html',  {'data':comosits})
    
         
         

    



@csrf_exempt
def  newproject(request):
    if request.method=='POST':
        received_json_data=    request.POST  
        
        
        jdata = '[{ "name": "JohnDoe",  "age": 30  }]'
        
        
        print(   received_json_data) 
    else:
        project_path = request.GET.get('path', '')
        file_path = request.GET.get('file', '')
        # print(project_path+"\\"+file_path+".json")  
        data = []
        with open(project_path+"\\"+file_path+".json") as file:
            data = json.load(file)
        
        project_data = []
        response  = requests.get('http://localhost:8000/projects/projects/?project_name='+file_path)
        if response.status_code == 200:
            # Access the response content (JSON, text, etc.)
            pdata =  response.json()
            if pdata:
                project_data = pdata
            else:
                pass
        else:
            print("Request failed with status code:", response.status_code)
        
        
        ''''thisi s for composestons of project'''
       
        for comosite in data:
            composits=[]            
            c_response  = requests.get('http://localhost:8000/projects/composit/?project='+str(project_data[0]["id"])+'&composite_name='+comosite["compositionName"])
            if c_response.status_code == 200:
                 composits =  c_response.json()
                 if not composits:
                    print(comosite["compositionName"])
                    composit_payload = {
                        "composite_name": comosite["compositionName"],
                        "composite_length": "",
                        "project": project_data[0]["id"]
                    }
                    url = "http://localhost:8000/projects/composit/"
                    response = requests.post(url, json=composit_payload)
                    composits[0] =response.json()
                  
           
            else:
                print("Request failed with status code:", response.status_code)
             
            for layer in comosite['layers']: 
                             
                if layer['properties']:
                    imagepath = ''
                    if layer['layerType'] == 'Image':
                       imagepath = layer['properties']['imageFilePath']

                    else:
                        print()
                        print(layer)
                        layer_payload = {
                            "layer_name": layer['layerName'],
                            "layer_type": layer['layerType'],
                            "layer_posx":layer['properties']['position'][0],
                            "layer_posy":layer['properties']['position'][1],
                            "layer_color": ', '.join(map(str, layer['properties']['color'])),
                            "fontFamily": '',
                            "text": layer['properties']['text'],
                            'scale':', '.join(map(str, layer['properties']['scale'])),
                            "layer_size": layer['properties']['size'],
                            "width": str(layer['properties']['width']),
                            "height":str(layer['properties']['height']),
                            "composit":composits[0]['id']
                        }
                         
                        url='http://localhost:8000/projects/pdata/'
                        response = requests.post(url, json=layer_payload)
                        layersdata =response.json()
                        print(layersdata)
                        print("------------------")

        
    return HttpResponse('Hello world')