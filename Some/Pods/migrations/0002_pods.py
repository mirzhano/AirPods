# Generated by Django 4.1.3 on 2022-11-17 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('image2', models.ImageField(upload_to='')),
                ('cost', models.IntegerField()),
            ],
        ),
    ]
