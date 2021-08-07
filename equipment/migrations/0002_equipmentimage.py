# Generated by Django 3.2.6 on 2021-08-07 23:13

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('caption', models.CharField(max_length=200, verbose_name='Текст слайда')),
                ('equipment', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='slides', to='equipment.equipemntpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]