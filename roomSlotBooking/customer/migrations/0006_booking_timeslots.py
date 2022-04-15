# Generated by Django 4.0.3 on 2022-04-15 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_remove_booking_timerslots_booking_rules'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='timeslots',
            field=models.CharField(choices=[('fullDay', 'fullday'), ('6am to 10am', '6am to 10am'), ('10am to 3pm', '10am to 3pm'), ('3pm to 10pm', '3pm to 10pm'), ('10pm to 6am', '10pm to 6am')], default=1, max_length=200),
            preserve_default=False,
        ),
    ]