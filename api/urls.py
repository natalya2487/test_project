# api/urls.py
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from purchases import viewsets as purchases_views

router = DefaultRouter()
router.register(r'material-types', purchases_views.MaterialTypeViewSet)
router.register(r'std-products', purchases_views.StdProdViewSet)
router.register(r'assemblies', purchases_views.AssemblyViewSet)
router.register(r'components', purchases_views.ComponentViewSet)
router.register(r'expendables', purchases_views.ExpendableViewSet)
router.register(r'material-expendables', purchases_views.MaterialExpendableViewSet)
router.register(r'std-prod-expendables', purchases_views.StdProdExpendableViewSet)
router.register(r'subcontract-action', purchases_views.SubcontractActionViewSet)
router.register(r'purchase-expendables', purchases_views.PurchaseViewSet)

urlpatterns = [
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('', include(router.urls)),
]
