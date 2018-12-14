from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView, CreateView, ListView, DeleteView


class FabUpdateView(SuccessMessageMixin, PermissionRequiredMixin, UpdateView):
    pass


class FabCreateView(SuccessMessageMixin, PermissionRequiredMixin, CreateView):
    pass


class FabListView(PermissionRequiredMixin, ListView):
    pass


class FabDeleteView(PermissionRequiredMixin, DeleteView):
    success_message = None

    def get_success_url(self):
        if self.success_message:
            messages.success(self.request, self.success_message)
        return super().get_success_url()
