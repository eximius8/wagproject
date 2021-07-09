# Generated by Django 3.2.5 on 2021-07-04 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0004_auto_20210704_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='bg_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]