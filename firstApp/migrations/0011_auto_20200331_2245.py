# Generated by Django 2.2.5 on 2020-03-31 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0010_auto_20200331_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carplan',
            name='finance_plan',
            field=models.CharField(default='unavailable', max_length=20),
        ),
        migrations.AlterField(
            model_name='carplan',
            name='plan_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='carplan',
            name='years_of_warranty',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='carspecs',
            name='car_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='firstApp.CarPlan'),
        ),
    ]
