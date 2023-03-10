# Generated by Django 4.1.7 on 2023-03-10 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lern', '0003_rename_course_lesson_course_set'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='owner_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner_course_get', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='owner_lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner_lesson_get', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
