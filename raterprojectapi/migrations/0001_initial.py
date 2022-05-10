# Generated by Django 4.0.4 on 2022-05-10 18:28

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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('description', models.CharField(max_length=55)),
                ('designer', models.CharField(max_length=55)),
                ('year_released', models.IntegerField()),
                ('number_of_players', models.IntegerField()),
                ('estimated_time_to_play', models.IntegerField()),
                ('age_recommendation', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=55)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.player')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.player')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pictureURL', models.CharField(max_length=500)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.player')),
            ],
        ),
        migrations.CreateModel(
            name='GameCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.category')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.game')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.player'),
        ),
    ]
