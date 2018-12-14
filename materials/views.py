from project.utils import FabUpdateView, FabListView, FabCreateView, FabDeleteView
from .models import Hardware


class HardwareList(FabListView):
    model = Hardware
    paginate_by = 30
    permission_required = "materials.view_hardware"

    def get_queryset(self):

        if self.request.user.is_superuser:
            queryset = Hardware.objects.all()
        else:
            queryset = Hardware.objects.filter(etablissement=self.request.user.etablissement)
        start_date = self.request.GET.get("start_date")
        end_date = self.request.GET.get("end_date")
        if start_date:
            queryset = queryset.filter(buy_date__gte=start_date)
        if end_date:
            queryset = queryset.filter(buy_date__lte=end_date)

        return queryset


class HardwareUpdateLight(FabUpdateView):
    model = Hardware
    fields = ["price"]
    success_url = "/"
    permission_required = "materials.change_hardware"
    success_message = "Hardware updated"

    def has_permission(self):
        return self.object.etablissement == self.request.user.etablissement


class HardwareUpdateComplete(FabUpdateView):
    model = Hardware
    fields = "__all__"
    success_url = "/"
    permission_required = "materials.change_hardware_plus"
    success_message = "Hardware updated"

    def has_permission(self):
        hardware = self.get_object()
        class_permission = super().has_permission()
        instance_permission = (hardware.etablissement == self.request.user.etablissement)
        return class_permission and instance_permission


class HardwareDelete(FabDeleteView):
    model = Hardware
    success_url = "/"
    permission_required = "materials.delete_hardware"


class HardwareCreate(FabCreateView):
    model = Hardware
    fields = "__all__"
    success_url = "/"
    permission_required = "materials.add_hardware"
    success_message = "New hardware created"
