from django.db import models

# Create your models here.



class ProjectsModel(models.Model):
    project_name = models.CharField(max_length=200)




class CompositsModel(models.Model):
    project = models.ForeignKey(ProjectsModel, on_delete=models.CASCADE)
    composite_name =  models.CharField(max_length=200, default='')
    composite_length =  models.CharField(max_length=200,  blank=True, null=True)

class LayersModel(models.Model):
    composit =  models.ForeignKey(CompositsModel, on_delete=models.CASCADE)
    layer_name =  models.CharField(max_length=200, blank=True, null=True)
    layer_type =  models.CharField(max_length=200,  blank=True, null=True)
    layer_posx =  models.CharField(max_length=200,  blank=True, null=True)
    layer_posy =  models.CharField(max_length=200,  blank=True, null=True)
    layer_color =  models.CharField(max_length=200,  blank=True, null=True)
    layer_size =  models.CharField(max_length=200,  blank=True, null=True)
    fontFamily =  models.CharField(max_length=200, blank=True, null=True)
    text =  models.CharField(max_length=200, blank=True, null=True)
    size =  models.CharField(max_length=200,  blank=True, null=True)
    width=  models.CharField(max_length=200,  blank=True, null=True)
    height=  models.CharField(max_length=200,  blank=True, null=True)
    image = models.FileField(upload_to='uploads/', blank=True, default='')
