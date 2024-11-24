# Generated by Django 5.1.3 on 2024-11-24 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('student_age', models.IntegerField()),
                ('student_description', models.TextField()),
                ('published_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]