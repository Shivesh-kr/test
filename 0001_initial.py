# Generated by Django 3.2.3 on 2021-05-23 18:04

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
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('lat', models.CharField(max_length=255)),
                ('lon', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=12)),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('incharge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reported_on', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='crime_images/')),
                ('description', models.TextField()),
                ('lat', models.CharField(max_length=255)),
                ('lon', models.CharField(max_length=255)),
                ('type', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Robbery'), (2, 'Fraud'), (3, 'Child Abuse'), (4, 'Murder'), (5, 'Cyber Crime')], null=True)),
                ('reviewd', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('reported_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='station.station')),
            ],
        ),
    ]
