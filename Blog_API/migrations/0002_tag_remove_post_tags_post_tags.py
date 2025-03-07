# Generated by Django 5.1.5 on 2025-01-24 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_API', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts_tags', to='Blog_API.tag'),
        ),
    ]
