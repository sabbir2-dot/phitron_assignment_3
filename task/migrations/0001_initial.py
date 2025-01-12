# Generated by Django 5.0.6 on 2024-07-03 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('task_description', models.TextField()),
                ('is_completed', models.BooleanField(default=False)),
                ('task_assign_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='category.category')),
            ],
        ),
    ]
