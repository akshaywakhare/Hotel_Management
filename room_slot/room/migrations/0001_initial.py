# Generated by Django 3.0.3 on 2021-04-07 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('hid', models.AutoField(primary_key=True, serialize=False)),
                ('hname', models.CharField(max_length=50)),
                ('hloc', models.CharField(max_length=50)),
                ('hotel_image', models.ImageField(default='0.jpeg', upload_to='media')),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Room_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rtype', models.CharField(choices=[('A', 'DELUXE'), ('B', 'SUITE'), ('C', 'RGWR')], max_length=1)),
                ('room_image', models.ImageField(default='0.jpeg', upload_to='media')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=10)),
                ('sprice', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rno', models.IntegerField()),
                ('hid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.Hotel')),
                ('rtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.Room_type')),
            ],
            options={
                'unique_together': {('rno', 'hid')},
            },
        ),
    ]
