from .api import ContactViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/contacts', ContactViewSet, 'contacts')

urlpatterns = router.urls