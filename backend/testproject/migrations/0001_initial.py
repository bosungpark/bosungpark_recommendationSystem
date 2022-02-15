# Generated by Django 3.2 on 2022-02-14 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='testData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('views_cnt', models.IntegerField(blank=True, null=True)),
                ('impressions_cnt', models.IntegerField(default=1)),
                ('text_length', models.IntegerField(blank=True, null=True)),
                ('image_cnt', models.IntegerField(blank=True, default=1, null=True)),
                ('like', models.IntegerField(blank=True, null=True)),
                ('importance', models.IntegerField(blank=True, default=0, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='testdata', to=settings.AUTH_USER_MODEL, verbose_name='테스트 데이터')),
            ],
        ),
    ]
