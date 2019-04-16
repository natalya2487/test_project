from django.contrib import admin

# Register your models here.
from .models import Action, Assembly, Expendable, Contract, Operation, StandardProductExpendable, MaterialExpendable, \
    RegularAction, SubcontractAction, StandardProduct, MaterialType, Component, Purchase

admin.site.register(Contract)
admin.site.register(Assembly)
admin.site.register(Component)
admin.site.register(Action)
admin.site.register(RegularAction)
admin.site.register(Operation)
admin.site.register(StandardProduct)
admin.site.register(MaterialType)
admin.site.register(Expendable)
admin.site.register(StandardProductExpendable)
admin.site.register(MaterialExpendable)
admin.site.register(SubcontractAction)
admin.site.register(Purchase)
