# Generated by Django 5.0.3 on 2024-05-20 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_is_subscribed_user_subscription_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='subscription_status',
            field=models.CharField(blank=True, default='unpaid', max_length=50),
        ),
    ]
