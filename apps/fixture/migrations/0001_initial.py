# Generated by Django 2.2 on 2020-06-17 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tournament', '0001_initial'),
        ('team', '0001_initial'),
    ]

    operations = [
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
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Tournament')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fixture.Venue')),
            ],
        ),
    ]
