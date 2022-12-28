# Generated by Django 4.0.5 on 2022-06-18 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_dictionary_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(blank=True, max_length=200, null=True)),
                ('translation', models.CharField(blank=True, max_length=200, null=True)),
                ('data_added', models.DateTimeField()),
                ('last_reviewed', models.DateTimeField()),
                ('times_reviewed', models.IntegerField()),
                ('successful_reviews', models.IntegerField()),
                ('notes', models.CharField(blank=True, max_length=500, null=True)),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.dictionary')),
            ],
        ),
    ]
