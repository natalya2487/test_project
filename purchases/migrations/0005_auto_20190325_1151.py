# Generated by Django 2.1.7 on 2019-03-25 11:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('purchases', '0004_auto_20190321_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalExpendable',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('stock_availability', models.IntegerField(blank=True, default=0)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('summ', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estimated_delivery', models.IntegerField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('assembly', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='purchases.Assembly')),
                ('component', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='purchases.Component')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical expendable',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AlterField(
            model_name='subcontractaction',
            name='expendable_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='purchases.Expendable'),
        ),
    ]