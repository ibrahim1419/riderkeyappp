from rest_framework import serializers

from ..models import (
    CashNds,
    Departments,
    Designations,
    Employees,
    Payslips,
    Performances,
    SalaryStructures,
    Teams,
    Timesheets,
)


class RelatedToNameField(serializers.RelatedField):
    def __init__(self, model=None, **kwargs):
        super().__init__(**kwargs)
        self.model = model

    def to_representation(self, instance):
        return instance.name

    def to_internal_value(self, data):
        obj = self.model.objects.get(name=data)

        if not obj:
            raise ValueError("Object not found")

        return obj


class EmployeeBaseSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True, required=False)
    cpr_image = serializers.ImageField(use_url=True, required=False)
    passport_image = serializers.ImageField(use_url=True, required=False)
    license_image = serializers.ImageField(use_url=True, required=False)
    visa_image = serializers.ImageField(use_url=True, required=False)


class EmployeesRetriveSerializer(EmployeeBaseSerializer):
    designation_id = RelatedToNameField(model=Designations, queryset=Designations.objects.all(), required=False)
    team_id = RelatedToNameField(model=Teams, queryset=Teams.objects.all(), required=False)
    department_id = RelatedToNameField(model=Departments, queryset=Departments.objects.all(), required=False)
    salary_structure = RelatedToNameField(model=SalaryStructures, queryset=SalaryStructures.objects.all())

    class Meta:
        model = Employees
        fields = (
            "id",
            "talabat_id",
            "name",
            "status",
            "designation_id",
            "team_id",
            "salary_structure",
            "department_id",
            "visa",
            "iban",
            "passport_number",
            "passport_expiry_date",
            "license",
            "license_expiry_date",
            "vehicle_type",
            "vehicle_make_model",
            "image",
            "cpr_image",
            "contract_file",
            "passport_image",
            "license_image",
            "visa_image",
        )


class EmployeesStaffSerializer(EmployeesRetriveSerializer):
    class Meta:
        model = Employees
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]


class EmployeesUpdateSerializer(EmployeeBaseSerializer):
    class Meta:
        model = Employees
        fields = (
            "image",
            "contact_numer",
            "visa",
            "passport_number",
            "passport_expiry_date",
            "license",
            "license_expiry_date",
            "vehicle_type",
            "vehicle_make_model",
            "cpr_image",
            "passport_image",
            "license_image",
            "visa_image",
        )


class TimesheetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timesheets
        fields = "__all__"


class PerformancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performances
        fields = "__all__"


class CashNdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashNds
        fields = "__all__"


class PaylipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payslips
        fields = "__all__"
