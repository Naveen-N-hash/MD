# Generated by Django 4.1.7 on 2023-03-31 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tvshows1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('rating', models.IntegerField()),
                ('seasons', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Seasons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_number', models.IntegerField()),
                ('tvshow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seasons_set', to='app.tvshows1')),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('rating', models.IntegerField()),
                ('embedded_link', models.URLField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Episodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode_name', models.CharField(max_length=100)),
                ('episode_number', models.IntegerField()),
                ('embedded_link', models.URLField()),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.seasons')),
            ],
        ),
    ]
