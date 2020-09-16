# Generated by Django 3.1 on 2020-09-12 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('showings', '0003_auto_20200903_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=200)),
                ('anilist_url', models.URLField()),
                ('ultrastar_url', models.URLField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=200)),
                ('related_series', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='showings.series')),
            ],
            options={
                'unique_together': {('title', 'artist')},
            },
        ),
        migrations.CreateModel(
            name='ArchivedRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ultrastar_url', models.URLField()),
                ('status', models.CharField(choices=[('completed', 'Completed'), ('cancelled', 'Cancelled')], max_length=16)),
                ('related_song', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='karaoke.song')),
            ],
        ),
    ]
