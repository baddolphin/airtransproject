# Generated by Django 3.0.3 on 2020-03-12 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('book_ref', models.AutoField(primary_key=True, serialize=False)),
                ('book_date', models.DateTimeField()),
                ('total_amount', models.FloatField()),
            ],
        ),
    ]