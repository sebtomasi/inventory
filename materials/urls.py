from django.urls import path

from materials.views import HardwareList, HardwareCreate, HardwareUpdateLight, HardwareUpdateComplete, HardwareDelete

app_name = 'materials'
urlpatterns = [
    path('', HardwareList.as_view(), name="hardware-list"),
    path('create/', HardwareCreate.as_view(), name="hardware-create"),
    path('edit/<int:pk>', HardwareUpdateLight.as_view(), name="hardware-update"),
    path('edit/complete/<int:pk>', HardwareUpdateComplete.as_view(), name="hardware-update-complete"),
    path('delete/<int:pk>', HardwareDelete.as_view(), name="hardware-delete"),

]
