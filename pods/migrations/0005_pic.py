# Generated by Django 4.1.3 on 2022-12-02 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pods', '0004_alter_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
