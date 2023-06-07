# Generated by Django 4.2.1 on 2023-06-07 06:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField()),
                ('rating', models.FloatField(blank=True, null=True)),
                ('purchase_link', models.CharField(blank=True, max_length=2000, null=True)),
                ('check_sample_link', models.CharField(blank=True, max_length=2000, null=True)),
                ('document', models.FileField(blank=True, null=True, upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]