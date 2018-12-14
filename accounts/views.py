from accounts.models import User
from project.utils import FabUpdateView, FabListView, FabDeleteView


class UserList(FabListView):
    model = User
    paginate_by = 30
    permission_required = "user.view_user"


class UserUpdate(FabUpdateView):
    model = User
    fields = ["first_name", "last_name", "email", "groups", "etablissement"]
    success_url = "/users"
    permission_required = "user.change_user"
    success_message = "User updated"


class UserDelete(FabDeleteView):
    model = User
    success_url = "/users"
    permission_required = "user.delete_user"
    success_message = "User deleted"

