# Generated by Django 3.0.5 on 2020-05-25 13:59

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
            name='Manage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('engineer', models.CharField(blank=True, max_length=256)),
                ('year', models.IntegerField(blank=True)),
                ('week', models.IntegerField(null=True)),
                ('task', models.CharField(blank=True, max_length=600)),
                ('comments', models.CharField(blank=True, max_length=700)),
                ('status', models.CharField(blank=True, max_length=256)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'weekly_update',
            },
        ),
    ]
