from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import InvoiceViewSet, UserViewSet
router = SimpleRouter()
router.register('users', UserViewSet)
router.register('', InvoiceViewSet)
urlpatterns = router.urls