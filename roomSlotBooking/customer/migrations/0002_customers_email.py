# Generated by Django 4.0.3 on 2022-04-15 16:26

from django.db import migrations, models
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='email',
            field=models.EmailField(max_length=254, null=sqlalchemy.sql.expression.true),
            preserve_default=sqlalchemy.sql.expression.true,
        ),
    ]
