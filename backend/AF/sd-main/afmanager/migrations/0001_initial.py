# Generated by Django 3.2.4 on 2023-07-04 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompositsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('composite_name', models.CharField(default='', max_length=200)),
                ('composite_length', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LayersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('layer_name', models.CharField(blank=True, max_length=200, null=True)),
                ('layer_type', models.CharField(blank=True, max_length=200, null=True)),
                ('layer_pos', models.CharField(blank=True, max_length=200, null=True)),
                ('layer_color', models.CharField(blank=True, max_length=200, null=True)),
                ('fontFamily', models.CharField(blank=True, max_length=200, null=True)),
                ('layer_size', models.CharField(blank=True, max_length=200, null=True)),
                ('width', models.CharField(blank=True, max_length=200, null=True)),
                ('height', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.FileField(blank=True, default='', upload_to='uploads/')),
                ('composit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afmanager.compositsmodel')),
            ],
        ),
        migrations.AddField(
            model_name='compositsmodel',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afmanager.projectsmodel'),
        ),
    ]
