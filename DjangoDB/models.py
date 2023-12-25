# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
highlighted = models.TextField()


def save(self, *args, **kwargs):
    """
    Use the `pygments` library to create a highlighted HTML
    representation of the code snippet.
    """
    lexer = get_lexer_by_name(self.language)
    linenos = 'table' if self.linenos else False
    options = {'title': self.title} if self.title else {}
    formatter = HtmlFormatter(style=self.style, linenos=linenos,
                              full=True, **options)
    self.highlighted = highlight(self.code, lexer, formatter)
    super().save(*args, **kwargs)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Clients(models.Model):
    client_id = models.AutoField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField(unique=True)
    phone_number = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'clients'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EmployeeSchedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    staff = models.ForeignKey('Staff', models.DO_NOTHING)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'employee_schedule'


class EventRooms(models.Model):
    event_room_id = models.AutoField(primary_key=True)
    event = models.ForeignKey('Events', models.DO_NOTHING)
    room = models.ForeignKey('Rooms', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'event_rooms'


class Events(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    client = models.ForeignKey(Clients, models.DO_NOTHING, blank=True, null=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=5, blank=True,
                                     null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'events'


class GuestHistory(models.Model):
    history_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Clients, models.DO_NOTHING)
    room = models.ForeignKey('Rooms', models.DO_NOTHING)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'guest_history'


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    item_desc = models.TextField()

    class Meta:
        managed = False
        db_table = 'inventory'


class InventoryRelationship(models.Model):
    room = models.OneToOneField('Rooms', models.DO_NOTHING,
                                primary_key=True)  # The composite primary key (room_id, inventory_id) found, that is not supported. The first column is selected.
    inventory = models.ForeignKey(Inventory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'inventory_relationship'


class Maintenance(models.Model):
    maintenance_id = models.AutoField(primary_key=True)
    room = models.ForeignKey('Rooms', models.DO_NOTHING)
    issue = models.TextField()
    date_reported = models.DateField()
    status = models.ForeignKey('Statuses', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'maintenance'


class Payments(models.Model):
    payment_id = models.AutoField(primary_key=True)
    reservation = models.ForeignKey('Reservations', models.DO_NOTHING, blank=True, null=True)
    event = models.ForeignKey(Events, models.DO_NOTHING, blank=True, null=True)
    payment_method = models.TextField()
    amount = models.DecimalField(max_digits=10,
                                 decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    payment_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payments'


class ReservationService(models.Model):
    reservation_service_id = models.AutoField(primary_key=True)
    reservation = models.ForeignKey('Reservations', models.DO_NOTHING)
    service = models.ForeignKey('Service', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'reservation_service'


class Reservations(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    room = models.ForeignKey('Rooms', models.DO_NOTHING)
    client = models.ForeignKey(Clients, models.DO_NOTHING)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    staff = models.ForeignKey('Staff', models.DO_NOTHING, blank=True, null=True)
    is_event = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'reservations'


class Reviews(models.Model):
    review_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Clients, models.DO_NOTHING)
    room = models.ForeignKey('Rooms', models.DO_NOTHING)
    rating = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviews'


class RoomFeatureRelationship(models.Model):
    room = models.OneToOneField('Rooms', models.DO_NOTHING,
                                primary_key=True)  # The composite primary key (room_id, feature_id) found, that is not supported. The first column is selected.
    feature = models.ForeignKey('RoomFeatures', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'room_feature_relationship'


class RoomFeatures(models.Model):
    feature_id = models.AutoField(primary_key=True)
    feature_name = models.TextField()
    feature_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room_features'


class Rooms(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_number = models.TextField(unique=True)
    room_type = models.TextField()
    rate = models.DecimalField(max_digits=10,
                               decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'rooms'


class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.TextField(unique=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'service'


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    position = models.TextField()

    class Meta:
        managed = False
        db_table = 'staff'


class Statuses(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.TextField()
    status_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statuses'
