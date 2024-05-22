# Generated by Django 5.0.4 on 2024-05-20 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0004_alter_subscription_sub_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='status',
            field=models.CharField(default='active', max_length=50),
        ),
        migrations.AlterField(
            model_name='subscriptionplan',
            name='plan_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]