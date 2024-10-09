# Generated by Django 5.1.1 on 2024-10-09 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_processor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_start_date', models.DateField()),
                ('policy_end_date', models.DateField()),
                ('policy_unique_id', models.IntegerField()),
                ('confirmation_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
