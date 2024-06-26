# Generated by Django 4.2.5 on 2024-02-21 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toyapp', '0010_profileuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryAgentApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('license_id', models.CharField(max_length=100)),
                ('license_image', models.ImageField(upload_to='license_images/')),
                ('experience', models.IntegerField()),
                ('profile_photo', models.ImageField(upload_to='profile_photos/')),
                ('applied_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
