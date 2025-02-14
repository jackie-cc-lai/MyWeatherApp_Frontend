# Generated by Django 2.2.5 on 2019-09-17 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('created', models.DateTimeField(auto_now=True)),
                ('weather', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('speed', models.DecimalField(decimal_places=2, max_digits=5)),
                ('deg', models.DecimalField(decimal_places=2, max_digits=5)),
                ('temp', models.DecimalField(decimal_places=2, max_digits=5)),
                ('temp_max', models.DecimalField(decimal_places=2, max_digits=5)),
                ('temp_min', models.DecimalField(decimal_places=2, max_digits=5)),
                ('icon', models.CharField(max_length=3)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
