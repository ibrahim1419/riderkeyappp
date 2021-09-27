from django.db import router
from django.urls import path
from rest_framework import routers
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register("employees", viewset=views.EmployeesViewSet)

urlpatterns = [
    path("timesheets/", views.GeneralList.as_view(), kwargs={"model_name": "timesheets"}),
    path("timesheets/<int:employee_id>/", views.GeneralList.as_view(), kwargs={"model_name": "timesheets"}),
    path(
        "timesheets/<int:employee_id>/<int:month>/<int:year>/",
        views.GeneralList.as_view(),
        kwargs={"model_name": "timesheets"},
    ),
    path("performances/", views.GeneralList.as_view(), kwargs={"model_name": "performances"}),
    path("performances/<int:employee_id>/", views.GeneralList.as_view(), kwargs={"model_name": "performances"}),
    path(
        "performances/<int:employee_id>/<int:month>/<int:year>/",
        views.GeneralList.as_view(),
        kwargs={"model_name": "performances"},
    ),
    path("cashnds/", views.GeneralList.as_view(), kwargs={"model_name": "cashnds"}),
    path("cashnds/<int:employee_id>/", views.GeneralList.as_view(), kwargs={"model_name": "cashnds"}),
    path(
        "cashnds/<int:employee_id>/<int:month>/<int:year>/",
        views.GeneralList.as_view(),
        kwargs={"model_name": "cashnds"},
    ),
    path("payslips/", views.GeneralList.as_view(), kwargs={"model_name": "payslips"}),
    path("payslips/<int:employee_id>/", views.GeneralList.as_view(), kwargs={"model_name": "payslips"}),
    path(
        "payslips/<int:employee_id>/<int:month>/<int:year>/",
        views.GeneralList.as_view(),
        kwargs={"model_name": "payslips"},
    ),
]

urlpatterns += router.urls
