# Generated by Django 5.0.1 on 2024-09-11 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0014_recordssubscriptionplan'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RecordsSubscriptionPlan',
        ),
        migrations.AddField(
            model_name='subscription',
            name='plan_name',
            field=models.CharField(default='Free', max_length=255),
        ),
    ]
