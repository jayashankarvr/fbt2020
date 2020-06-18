# Generated by Django 2.2.13 on 2020-06-18 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0002_delete_fixture'),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='tournament',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='tournament.Tournament'),
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
