from django.urls import path
from .views import login_user, CreateFormView, UserdataListView

app_name = 'base_app'

urlpatterns = [
    path('', CreateFormView.as_view(), name="form"),
    path('authorization/', login_user, name="authorization"),
    path('get_data/', UserdataListView.as_view(), name="get_user_data")
]
