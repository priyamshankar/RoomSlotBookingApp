# Generated by Django 4.0.3 on 2022-04-15 17:31

from django.db import migrations, models
import django.db.models.deletion
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_booking_manager_records_room_rules'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='records',
            name='cName',
        ),
        migrations.RemoveField(
            model_name='records',
            name='dateBooked',
        ),
        migrations.RemoveField(
            model_name='records',
            name='email',
        ),
        migrations.RemoveField(
            model_name='records',
            name='timerslots',
        ),
        migrations.RemoveField(
            model_name='records',
            name='userId',
        ),
        migrations.AddField(
            model_name='booking',
            name='Customers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.customers'),
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.room'),
        ),
        migrations.AddField(
            model_name='records',
            name='Customers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.customers'),
        ),
        migrations.AddField(
            model_name='records',
            name='booking',
            field=models.ForeignKey(null=sqlalchemy.sql.expression.true, on_delete=django.db.models.deletion.SET_NULL, to='customer.booking'),
            preserve_default=sqlalchemy.sql.expression.true,
        ),
        migrations.AddField(
            model_name='records',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.room'),
        ),
    ]
