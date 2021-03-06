# Generated by Django 2.2.13 on 2020-06-18 03:46

import apps.tournament.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(default=apps.tournament.models.now_plus_30)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_time', models.DateTimeField()),
                ('a_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='a_fixture', to='team.Team')),
                ('b_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='b_fixture', to='team.Team')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fixtures', to='tournament.Tournament')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Venue')),
            ],
        ),
    ]
