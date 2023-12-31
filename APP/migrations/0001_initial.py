# Generated by Django 4.2.1 on 2023-06-23 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodInsert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Food_id', models.CharField(max_length=20)),
                ('Customer_name', models.CharField(max_length=20)),
                ('Product_name', models.CharField(max_length=20)),
                ('Product_quntity', models.CharField(max_length=20)),
                ('Product_prize', models.FloatField()),
                ('address', models.TextField()),
                ('Date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='userfeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('rating', models.IntegerField()),
                ('feedback', models.TextField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]
