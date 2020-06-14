# Generated by Django 2.2.5 on 2020-04-01 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0016_auto_20200401_0947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carplan',
            old_name='finance_plan',
            new_name='finanace_plan',
        ),
        migrations.AlterField(
            model_name='carspecs',
            name='car_plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='firstApp.CarPlan'),
        ),
    ]
