from rest_framework.routers import SimpleRouter

from ads.views.cat import CategoryViewSet

router = SimpleRouter()
router.register('', CategoryViewSet)

urlpatterns = []

urlpatterns += router.urls
