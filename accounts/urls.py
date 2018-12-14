




from django.urls import path, include

from accounts.views import UserList, UserUpdate, UserDelete

app_name = 'accounts'
urlpatterns = [
    path('users/', UserList.as_view(), name="user-list"),
    path('users/edit/<int:pk>', UserUpdate.as_view(), name="user-update"),
    path('users/delete/<int:pk>', UserDelete.as_view(), name="user-delete"),
    path('', include('django.contrib.auth.urls')),

]
