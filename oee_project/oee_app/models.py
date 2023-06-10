from django.db import models

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class DashboardAlertrules(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    cam_name = models.CharField(max_length=150, blank=True, null=True)
    rulejson = models.TextField(db_column='ruleJson')  # Field name made lowercase.
    img_ref = models.TextField()
    json_formated = models.TextField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dashboard_alertrules'


class DashboardAudioDevices(models.Model):
    device_id = models.CharField(max_length=200)
    cam_name = models.CharField(max_length=100)
    device_name = models.CharField(max_length=100)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dashboard_audio_devices'


class DashboardAutoDelete(models.Model):
    name = models.CharField(max_length=100)
    file_name = models.CharField(max_length=100)
    expire_time = models.IntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dashboard_auto_delete'


class DashboardBatchprocessing(models.Model):
    filepath = models.CharField(db_column='filePath', max_length=100)  # Field name made lowercase.
    camname = models.CharField(db_column='camName', max_length=100)  # Field name made lowercase.
    starttime = models.CharField(db_column='startTime', max_length=100)  # Field name made lowercase.
    endtime = models.CharField(db_column='endTime', max_length=100)  # Field name made lowercase.
    batchstarttime = models.CharField(db_column='BatchStartTime', max_length=100)  # Field name made lowercase.
    batchendtime = models.CharField(db_column='BatchEndTime', max_length=100)  # Field name made lowercase.
    batchsize = models.CharField(db_column='BatchSize', max_length=100)  # Field name made lowercase.
    fps = models.CharField(db_column='Fps', max_length=100)  # Field name made lowercase.
    status = models.CharField(max_length=100)
    xmlmodel = models.CharField(db_column='xmlModel', max_length=100)  # Field name made lowercase.
    modelname = models.CharField(db_column='modelName', max_length=100)  # Field name made lowercase.
    location = models.CharField(max_length=100)
    beamcount = models.CharField(max_length=100)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dashboard_batchprocessing'


class DashboardCamError(models.Model):
    cam_name = models.CharField(max_length=100)
    reason = models.CharField(max_length=100)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dashboard_cam_error'


class DashboardCamera(models.Model):
    camname = models.CharField(db_column='camName', max_length=100)  # Field name made lowercase.
    source = models.CharField(max_length=100)
    edge_device = models.CharField(max_length=100)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dashboard_camera'


class DashboardCamerafilters(models.Model):
    camname = models.CharField(db_column='camName', max_length=100)  # Field name made lowercase.
    actions = models.CharField(max_length=100)
    action_params = models.CharField(max_length=3000)
    edge_device = models.CharField(max_length=100)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dashboard_camerafilters'


class DashboardDevice(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)
    mac_address = models.CharField(max_length=100)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dashboard_device'


class DashboardGoalTarget(models.Model):
    cam_name = models.CharField(max_length=100)
    shift = models.CharField(max_length=100)
    target = models.CharField(max_length=100)
    value = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dashboard_goal_target'


class DashboardPasswordreset(models.Model):
    email = models.CharField(max_length=150)
    otp = models.CharField(max_length=150)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dashboard_passwordreset'


class DashboardPlannedStop(models.Model):
    reason = models.CharField(max_length=200)
    shift = models.CharField(max_length=200, blank=True, null=True)
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dashboard_planned_stop'


class DashboardProcess(models.Model):
    cycle_no = models.IntegerField()
    unique_id = models.CharField(max_length=100)
    process_name = models.CharField(max_length=100)
    cam_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    shift = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    info = models.CharField(max_length=300)
    time = models.DateTimeField()
    alert = models.CharField(max_length=100)
    event = models.CharField(max_length=100)
    downtime = models.CharField(max_length=100)
    image_path = models.CharField(max_length=300)
    downtime_category = models.CharField(max_length=100)
    downtime_reason = models.CharField(max_length=200)
    downtime_reason_detect = models.CharField(max_length=200)
    downtime_entry_type = models.BooleanField()
    alert_threshold = models.CharField(max_length=200)
    alert_actual = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'dashboard_process'


class DashboardProcessMapData(models.Model):
    json = models.TextField()
    edge_id = models.CharField(max_length=100)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dashboard_process_map_data'


class DashboardProcessMapDataCheckpoint(models.Model):
    json = models.TextField()
    time = models.DateTimeField()
    edge_id = models.ForeignKey(DashboardProcessMapData, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboard_process_map_data_checkpoint'


class DashboardProcessNames(models.Model):
    process_name = models.CharField(max_length=150)
    device_id = models.CharField(max_length=150)
    process_type = models.CharField(max_length=150)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dashboard_process_names'


class DashboardProfile(models.Model):
    display_name = models.CharField(max_length=150, blank=True, null=True)
    profile_image = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    website = models.CharField(max_length=150, blank=True, null=True)
    time = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboard_profile'


class DashboardShift(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)
    start_time = models.CharField(max_length=150, blank=True, null=True)
    end_time = models.CharField(max_length=150, blank=True, null=True)
    start_day = models.BooleanField(blank=True, null=True)
    end_day = models.BooleanField(blank=True, null=True)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dashboard_shift'


class DashboardSmtpbackendconfig(models.Model):
    host = models.CharField(max_length=100)
    port = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    senderlist = models.CharField(db_column='senderList', max_length=1000)  # Field name made lowercase.
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dashboard_smtpbackendconfig'


class DashboardUiTheme(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    value = models.CharField(max_length=250, blank=True, null=True)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dashboard_ui_theme'


class DashboardUserDashboard(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    template = models.CharField(max_length=100)
    process_name = models.CharField(max_length=1000)
    chart_type = models.CharField(max_length=100)
    x_axis = models.CharField(max_length=100)
    y_axis = models.CharField(max_length=100)
    card_tooltip = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'dashboard_user_dashboard'


class DashboardUserpermission(models.Model):
    username = models.TextField()
    user_access = models.CharField(max_length=500)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dashboard_userpermission'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

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

class Machine(models.Model):
    name = models.CharField(max_length=100)

class ProductionLog(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    cycle_id = models.CharField(max_length=100, unique=True)
    date_time = models.DateTimeField()
    units_produced = models.PositiveIntegerField()
