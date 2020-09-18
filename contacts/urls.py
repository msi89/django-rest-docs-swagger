from django.urls import path, include
from rest_framework.routers import DefaultRouter
from contacts import views


router = DefaultRouter()
router.register('', views.ContactViewset)
urlpatterns = router.urls


# urlpatterns = [
#     # path('', include(router.urls))
#     path('', views.ContactViewset.as_view({'get': 'list'})),
#     path('', views.ContactViewset.as_view({'get': 'create'})),
#     path('<int:pk>',
#          views.ContactViewset.as_view({'get': 'retrieve'})),
# ]
