# Generated by Django 5.1.1 on 2024-10-09 10:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_processor', '0004_plan'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insured',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insured_id', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance_processor.organization')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance_processor.plan')),
                ('policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance_processor.policy')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
