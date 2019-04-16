from django.db import models

from simple_history.models import HistoricalRecords


# Create your models here.
class Contract(models.Model):
    name = models.CharField(max_length=50)


class StandardProduct(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)


class MaterialType(models.Model):
    name = models.CharField(max_length=50)


class Assembly(models.Model):
    name = models.CharField(max_length=50)


class Component(models.Model):
    name = models.CharField(max_length=50)


class Operation(models.Model):
    name = models.CharField(max_length=50)


class Expendable(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    assembly = models.ForeignKey(Assembly, on_delete=models.PROTECT, null=True, blank=True)
    component = models.ForeignKey(Component, on_delete=models.PROTECT, null=True, blank=True)
    stock_availability = models.IntegerField(default=0, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    summ = models.DecimalField(max_digits=10, decimal_places=2)
    estimated_delivery = models.IntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    history = HistoricalRecords()

class MaterialExpendable(Expendable):
    material = models.ForeignKey(MaterialType, on_delete=models.PROTECT)
    symbol = models.CharField(max_length=10)
    diameter = models.IntegerField(null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)


class StandardProductExpendable(Expendable):
    std_prod = models.ForeignKey(StandardProduct, on_delete=models.PROTECT)


class Purchase(models.Model):
    expendable = models.ForeignKey(Expendable, on_delete=models.PROTECT)


class Action(models.Model):
    operation = models.ForeignKey(Operation, on_delete=models.PROTECT)


class RegularAction(Action):
    duration = models.IntegerField()


class SubcontractManager(models.Manager):
    def create_book(self, title):
        book = self.create(title=title)
        # do something with the book
        return book


class SubcontractAction(Action):
    expendable_ptr = models.OneToOneField(
        Expendable, on_delete=models.CASCADE,
        # parent_link=True,
    )
    contract = models.ForeignKey(Contract, on_delete=models.PROTECT)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if force_insert:
            print('insert')
        if force_update:
            print('update')
        super().save(force_insert, force_update, using,
                     update_fields)


# SubcontractAction.objects.create()
# SubcontractAction.objects.update()