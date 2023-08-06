from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect


def redirectToApp(request):
    return HttpResponseRedirect("/todo")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", redirectToApp, name="index"),
    path("todo/", include("todo.urls")),
    path("accounts/", include("accounts.urls")),
]