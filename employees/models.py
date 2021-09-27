from cloudinary.models import CloudinaryField
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class SalaryStructures(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    hourly_rate = models.CharField(max_length=255)
    per_drop = models.CharField(max_length=256, blank=True, null=True)
    houry_rate_temp = models.CharField(max_length=256, blank=True, null=True)
    delivery_rate = models.CharField(max_length=255)
    extra_per_utr = models.CharField(max_length=45, blank=True, null=True)
    per_km = models.CharField(max_length=45, blank=True, null=True)
    long_distance_1 = models.CharField(max_length=45, blank=True, null=True)
    long_distance_2 = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    overtime_rate = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "salary_structures"

    def __str__(self) -> str:
        return self.name


from django.db import models


class AccountCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "account_categories"


class AccountTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    accounttypename = models.CharField(db_column="accountTypeName", max_length=255)  # Field name made lowercase.
    subaccount = models.IntegerField(db_column="subAccount", blank=True, null=True)  # Field name made lowercase.
    account_category = models.ForeignKey(AccountCategories, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "account_types"


class Accounts(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column="Name", max_length=256, blank=True, null=True)  # Field name made lowercase.
    balance = models.IntegerField(default=0)
    holderid = models.IntegerField(db_column="holderID", default=1)  # Field name made lowercase.
    account_category = models.ForeignKey(AccountCategories, models.DO_NOTHING, blank=True, null=True)
    account_type = models.ForeignKey(AccountTypes, models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey("Employees", models.CASCADE, blank=True, null=True)
    supplier_id = models.PositiveBigIntegerField(blank=True, null=True)
    customer_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "accounts"


class Designations(models.Model):
    id = models.BigAutoField(primary_key=True)
    department_id = models.IntegerField()
    name = models.CharField(max_length=255)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "designations"

    def __str__(self) -> str:
        return self.name


class Departments(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "departments"

    def __str__(self) -> str:
        return self.name


class Teams(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    team_leader = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "teams"

    def __str__(self) -> str:
        return self.name


class Employees(models.Model):
    BANK_TYPE_CHOICES = (("Bank", _("Bank")), ("TAM", _("TAM")))
    VEHICLE_TYPE_CHOICES = (
        ("Car", _("Car")),
        ("Bike", _("Bike")),
        ("Motorbike", _("Motorbike")),
        ("Motor", _("Motor")),
        ("HATCHBACK", _("HATCHBACK")),
    )
    COUNTRY_CHOICES = (("bahrain", _("Bahrain")), ("erbil", _("Erbil")), ("dubai", ("Dubai")), ("iraq", _("Iraq")))
    VISA_TYPE_CHOICES = (
        ("Flexi Visa", _("Flexi Visa")),
        ("notflexi", _("Not Flexi")),
        ("KA Visa", _("KA Visa")),
        ("Free Visa", _("Free Visa")),
    )
    VERIFIED_CHOICES = (("no", _("No")), ("IBAN Verified", _("IBAN Verified")))
    STATUS_CHOICES = (
        ("Active", _("Active")),
        ("inactive", _("Inactive")),
        ("Salary Suspended", _("Salary Suspended")),
        ("Terminated", _("Terminated")),
        ("vacation", _("Vacation")),
    )

    id = models.BigAutoField(primary_key=True)
    user_id = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="employee",
        db_constraint=False,
        db_column="user_id",
    )
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    verified = models.CharField(max_length=255, default="No", choices=VERIFIED_CHOICES)
    status = models.CharField(max_length=255, default="Active", choices=STATUS_CHOICES)
    bank_type = models.CharField(max_length=45, choices=BANK_TYPE_CHOICES, blank=True, null=True)
    contact_numer = models.CharField(max_length=255, blank=True, null=True)
    cpr = models.CharField(unique=True, max_length=255)
    talabat_id = models.CharField(unique=True, max_length=255)
    type = models.CharField(max_length=255, blank=True, null=True)
    branch_id = models.IntegerField(blank=True, null=True)
    department_id = models.ForeignKey(
        to="Departments",
        on_delete=models.DO_NOTHING,
        db_column="department_id",
        db_constraint=False,
        blank=True,
        null=True,
        related_name="department_employees",
    )
    designation_id = models.ForeignKey(
        to="Designations",
        on_delete=models.DO_NOTHING,
        db_column="designation_id",
        db_constraint=False,
        blank=True,
        null=True,
        related_name="designation_employees",
    )
    team_id = models.ForeignKey(
        to="Teams",
        on_delete=models.DO_NOTHING,
        db_column="team_id",
        db_constraint=False,
        blank=True,
        null=True,
        related_name="team_employees",
    )
    visa = models.CharField(max_length=255, choices=VISA_TYPE_CHOICES, blank=True, null=True)
    visa_expiry_date = models.DateField(blank=True, null=True)
    contract_start = models.DateField(blank=True, null=True)
    contract_end = models.DateField(blank=True, null=True)
    joining_date = models.DateField(blank=True, null=True)
    vehicle_type = models.CharField(max_length=255, choices=VEHICLE_TYPE_CHOICES, blank=True, null=True)
    vehicle_number = models.CharField(max_length=255, blank=True, null=True)
    vehicle_make_model = models.CharField(max_length=255, blank=True, null=True)
    vehicle_year = models.CharField(max_length=255, blank=True, null=True)
    license = models.CharField(max_length=255, blank=True, null=True)
    license_expiry_date = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=128, choices=COUNTRY_CHOICES, blank=True, null=True)
    bank_account_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    cpr_image = CloudinaryField(blank=True, null=True)
    image = CloudinaryField(blank=True, null=True)
    passport_image = CloudinaryField(blank=True, null=True)
    license_image = CloudinaryField(blank=True, null=True)
    visa_image = CloudinaryField(blank=True, null=True)
    contract_file = models.FileField(max_length=255, blank=True, null=True)
    passport_number = models.CharField(unique=True, max_length=255, blank=True, null=True)
    passport_expiry_date = models.DateField(blank=True, null=True)
    salary_structure = models.ForeignKey("SalaryStructures", models.DO_NOTHING, db_column="salary_structure")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    iban = models.CharField(max_length=255, blank=True, null=True)
    cnd = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = "employees"


class Timesheets(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    hours = models.CharField(max_length=255)
    orders = models.CharField(max_length=255, blank=True, null=True)
    utr = models.CharField(max_length=45, blank=True, null=True)
    po_orders = models.CharField(max_length=256)
    po_hours = models.CharField(max_length=256)
    day_deduction = models.CharField(max_length=255, blank=True, null=True)
    pay_per_distance = models.CharField(max_length=45, blank=True, null=True)
    extra_per_utr = models.CharField(max_length=45, blank=True, null=True)
    day_deduction_rate = models.CharField(max_length=255, blank=True, null=True)
    double_orders = models.CharField(max_length=255, blank=True, null=True)
    long_distance_sakhir = models.CharField(max_length=45, blank=True, null=True)
    long_distance_durra = models.CharField(max_length=45, blank=True, null=True)
    month = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    employee = models.ForeignKey("Employees", models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = "timesheets"


class Performances(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee = models.ForeignKey("Employees", models.CASCADE, blank=True, null=True)
    starting_date = models.CharField(max_length=255)
    ending_date = models.CharField(max_length=255)
    shift_count = models.CharField(max_length=255)
    no_shows = models.CharField(max_length=255)
    late_login = models.CharField(max_length=255)
    completed_orders = models.CharField(max_length=255)
    cancelled_orders = models.CharField(max_length=255)
    cancellation_10_orders = models.CharField(max_length=255)
    utr = models.CharField(max_length=255)
    total_working_hours = models.CharField(max_length=255)
    total_break_hours = models.CharField(max_length=255)
    attendance_percentage = models.CharField(max_length=255)
    breaks_percentage = models.CharField(max_length=255)
    notification_count = models.CharField(max_length=255)
    acceptance_count = models.CharField(max_length=255)
    acceptance_rate = models.CharField(max_length=255)
    avg_customer_time = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = "performances"


class CashNds(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee = models.ForeignKey("Employees", models.CASCADE, blank=True, null=True)
    previous_date = models.CharField(max_length=255)
    previous_pending = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    previous_deposit = models.DecimalField(max_digits=5, decimal_places=2)
    previous_balance = models.DecimalField(max_digits=5, decimal_places=2)
    bonus = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    bonus_type = models.CharField(max_length=255, blank=True, null=True)
    date_selected = models.CharField(max_length=255)
    date_cod = models.DecimalField(max_digits=5, decimal_places=2)
    date_pending = models.DecimalField(max_digits=5, decimal_places=2)
    deposit_status = models.CharField(max_length=255)
    deposit_delayed = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = "cash_nds"


class Payslips(models.Model):
    id = models.BigAutoField(primary_key=True)
    basic_salary = models.CharField(max_length=45, blank=True, null=True)
    bonus = models.CharField(max_length=45, blank=True, null=True)
    deduction = models.CharField(max_length=45, blank=True, null=True)
    net_payable = models.CharField(max_length=255)
    salary_month = models.CharField(max_length=255)
    payroll_entry_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    employee = models.ForeignKey("Employees", models.CASCADE, blank=True, null=True)
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = "payslips"
