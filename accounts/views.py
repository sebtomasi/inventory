from django.contrib.auth.mixins import PermissionRequiredMixin

from django.views.generic import ListView, UpdateView, DeleteView
from accounts.models import User

class UserList(PermissionRequiredMixin, ListView):
    model = User
    paginate_by = 30
    permission_required = "user.view_user"


class UserUpdate(PermissionRequiredMixin, UpdateView):
    model = User
    fields = ["first_name", "last_name", "email", "groups","etablissement"]
    success_url = "/users"
    permission_required = "user.change_user"


class UserDelete(PermissionRequiredMixin, DeleteView):
    model = User
    success_url = "/users"
    permission_required = "user.delete_user"
