# Generated by Django 3.2.5 on 2021-11-01 17:59

import api.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access', models.CharField(default='only_author', max_length=50, verbose_name='Access')),
                ('file', models.FileField(upload_to=api.models.upload_to, verbose_name='File')),
                ('download_count', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Download counter')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'Files',
                'ordering': ['-download_count'],
            },
        ),
    ]
