# Generated by Django 2.2.7 on 2019-12-01 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempuser',
            name='desired_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.RoomCandidate'),
        ),
        migrations.AddField(
            model_name='tempuser',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.University'),
        ),
        migrations.AddField(
            model_name='registerform',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Activity'),
        ),
        migrations.AddField(
            model_name='registerform',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.University'),
        ),
    ]