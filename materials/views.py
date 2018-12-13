from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, UpdateView, DeleteView

from .models import Hardware


class HardwareList(PermissionRequiredMixin, ListView):
    model = Hardware
    paginate_by = 30
    permission_required = "materials.view_hardware"

    def get_queryset(self):
        return Hardware.objects.filter(etablissement=self.request.user.etablissement)


class HardwareUpdateLight(PermissionRequiredMixin, UpdateView):
    model = Hardware
    fields = ["price"]
    success_url = "/"
    permission_required = "materials.change_hardware"


    def has_permission(self):
        return self.object.etablissement == self.request.user.etablissement


class HardwareUpdateComplete(PermissionRequiredMixin, UpdateView):
    model = Hardware
    fields = "__all__"
    success_url = "/"
    permission_required = "materials.change_hardware_plus"

    def has_permission(self):
        hardware = self.get_object()
        class_permission = super().has_permission()
        instance_permission = (hardware.etablissement == self.request.user.etablissement)
        return class_permission and instance_permission


class HardwareDelete(PermissionRequiredMixin, DeleteView):
    model = Hardware
    success_url = "/"
    permission_required = "materials.delete_hardware"
