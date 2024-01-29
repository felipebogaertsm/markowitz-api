from django.urls import path

from optimizer.views import optimizer_api

urlpatterns = [
    path(
        "",
        optimizer_api,
        name="markowitz-optimizer-api",
    ),
]
