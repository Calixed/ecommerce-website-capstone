# Generated by Django 3.2.3 on 2021-10-20 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20211020_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.order'),
        ),
    ]
