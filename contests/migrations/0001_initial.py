# Generated by Django 5.2 on 2025-05-07 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('duration_minutes', models.PositiveIntegerField(default=150)),
                ('end_time', models.DateTimeField(blank=True)),
                ('is_public', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('division', models.CharField(choices=[('Div1', 'Division 1'), ('Div2', 'Division 2'), ('Div3', 'Division 3'), ('Div4', 'Division 4'), ('Open', 'Open for All')], default='Open', max_length=10)),
                ('rated', models.BooleanField(default=True)),
                ('visibility', models.CharField(choices=[('public', 'Public'), ('private', 'Private')], default='public', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'contest',
            },
        ),
    ]
