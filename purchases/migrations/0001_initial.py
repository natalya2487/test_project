# Generated by Django 2.1.7 on 2019-03-15 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assembly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Expendable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('stock_availability', models.IntegerField(blank=True, default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('summ', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StandardProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialExpendable',
            fields=[
                ('expendable_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='purchases.Expendable')),
                ('symbol', models.CharField(max_length=10)),
                ('diameter', models.IntegerField(blank=True, null=True)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='purchases.MaterialType')),
            ],
            bases=('purchases.expendable',),
        ),
        migrations.CreateModel(
            name='StandardProductExpendable',
            fields=[
                ('expendable_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='purchases.Expendable')),
                ('symbol', models.CharField(max_length=10)),
                ('diameter', models.IntegerField(blank=True, null=True)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('std_prod', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='purchases.StandardProduct')),
            ],
            bases=('purchases.expendable',),
        ),
        migrations.AddField(
            model_name='expendable',
            name='assembly',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='purchases.Assembly'),
        ),
        migrations.AddField(
            model_name='expendable',
            name='component',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='purchases.Component'),
        ),
    ]
