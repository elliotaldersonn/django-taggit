# Generated by Django 2.2.5 on 2020-05-14 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DemoFormm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('msg', models.TextField()),
                ('slug', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
