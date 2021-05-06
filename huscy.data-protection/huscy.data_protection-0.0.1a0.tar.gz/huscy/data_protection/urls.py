from rest_framework.routers import DefaultRouter

from huscy.data_protection import views


router = DefaultRouter()
router.register('subjects', views.SubjectViewSet)


urlpatterns = router.urls
