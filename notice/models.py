# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

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
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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


class NoticeAuthor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'notice_author'


class NoticeDictMod(models.Model):
    item = models.CharField(max_length=100)
    value = models.CharField(max_length=30)
    caption = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'notice_dict_mod'


class NoticePublisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'notice_publisher'


class NoticeTbCar(models.Model):
    carnum = models.CharField(max_length=500)
    carattr = models.CharField(max_length=500)
    carsize = models.CharField(max_length=500)
    begin1 = models.DateTimeField()
    end1 = models.DateTimeField()
    begin2 = models.DateTimeField()
    end2 = models.DateTimeField()
    inrecid = models.CharField(max_length=500)
    outrecid = models.CharField(max_length=500)
    intime = models.DateTimeField()
    outime = models.DateTimeField()
    tpriceid = models.CharField(max_length=500)
    expired1 = models.CharField(max_length=500)
    expired2 = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'notice_tb_car'


class TbAreadev(models.Model):
    devid = models.IntegerField(primary_key=True)
    devstate = models.IntegerField(blank=True, null=True)
    online = models.IntegerField(blank=True, null=True)
    devname = models.CharField(max_length=20, blank=True, null=True)
    ip = models.CharField(max_length=20, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    a_areaid = models.IntegerField(db_column='A_areaid', blank=True, null=True)  # Field name made lowercase.
    b_areaid = models.IntegerField(db_column='B_areaid', blank=True, null=True)  # Field name made lowercase.
    devcode = models.CharField(max_length=20, blank=True, null=True)
    serialcode = models.CharField(max_length=20, blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_areadev'


class TbCamera(models.Model):
    devid = models.IntegerField(primary_key=True)
    gateid = models.IntegerField(blank=True, null=True)
    devstate = models.IntegerField(blank=True, null=True)
    online = models.IntegerField(blank=True, null=True)
    devname = models.CharField(max_length=20, blank=True, null=True)
    cameratype = models.IntegerField(blank=True, null=True)
    cameramodel = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=20, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    devcode = models.CharField(max_length=20, blank=True, null=True)
    serialcode = models.CharField(max_length=20, blank=True, null=True)
    activecode = models.CharField(max_length=20, blank=True, null=True)
    activestate = models.IntegerField(blank=True, null=True)
    version = models.CharField(max_length=20, blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)
    streamaddr = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_camera'


class TbCar(models.Model):
    carnum = models.CharField(primary_key=True, max_length=20)
    objstate = models.IntegerField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    carmodel = models.CharField(max_length=20, blank=True, null=True)
    carattr = models.IntegerField(blank=True, null=True)
    carsize = models.IntegerField(blank=True, null=True)
    carcolor = models.IntegerField(blank=True, null=True)
    carpic = models.BinaryField(blank=True, null=True)
    platetype = models.IntegerField(blank=True, null=True)
    platecolor = models.IntegerField(blank=True, null=True)
    platepic = models.BinaryField(blank=True, null=True)
    regdate = models.DateTimeField(blank=True, null=True)
    begin1 = models.DateTimeField(blank=True, null=True)
    end1 = models.DateTimeField(blank=True, null=True)
    expired1 = models.IntegerField(blank=True, null=True)
    begin2 = models.DateTimeField(blank=True, null=True)
    end2 = models.DateTimeField(blank=True, null=True)
    expired2 = models.IntegerField(blank=True, null=True)
    areaid = models.IntegerField(blank=True, null=True)
    inrecid = models.IntegerField(blank=True, null=True)
    intime = models.DateTimeField(blank=True, null=True)
    outrecid = models.IntegerField(blank=True, null=True)
    outime = models.DateTimeField(blank=True, null=True)
    staydays = models.IntegerField(blank=True, null=True)
    stayhours = models.IntegerField(blank=True, null=True)
    stayminutes = models.IntegerField(blank=True, null=True)
    payrecid = models.IntegerField(blank=True, null=True)
    paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    paidtime = models.DateTimeField(blank=True, null=True)
    pkcount = models.IntegerField(blank=True, null=True)
    balance = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    shopcutid = models.IntegerField(blank=True, null=True)
    selflock = models.IntegerField(blank=True, null=True)
    locktime = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)
    opname = models.CharField(max_length=20, blank=True, null=True)
    mpaid1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    mpaid2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    carnumref1 = models.CharField(max_length=20, blank=True, null=True)
    carnumref2 = models.CharField(max_length=20, blank=True, null=True)
    pkcardid = models.CharField(max_length=20, blank=True, null=True)
    passcheck = models.IntegerField(blank=True, null=True)
    passmode = models.IntegerField(blank=True, null=True)
    gategroupid = models.IntegerField(blank=True, null=True)
    innerareaid = models.IntegerField(blank=True, null=True)
    innerintime = models.DateTimeField(blank=True, null=True)
    inneroutime = models.DateTimeField(blank=True, null=True)
    paidsum = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    paiddate = models.DateTimeField(blank=True, null=True)
    expbegin = models.DateTimeField(blank=True, null=True)
    expend = models.DateTimeField(blank=True, null=True)
    expired = models.IntegerField(blank=True, null=True)
    carhide = models.IntegerField(blank=True, null=True)
    carlife = models.IntegerField(blank=True, null=True)
    carpswd = models.CharField(max_length=20, blank=True, null=True)
    carpswdmd5 = models.CharField(max_length=32, blank=True, null=True)
    paid_cash = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    s_cat = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    w_cat = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    payrectime = models.DateTimeField(blank=True, null=True)
    mpriceid = models.IntegerField(blank=True, null=True)
    tpriceid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_car'


class TbCard(models.Model):
    cardid = models.IntegerField(primary_key=True)
    objstate = models.IntegerField(blank=True, null=True)
    cardcode = models.CharField(max_length=20, blank=True, null=True)
    cardattr = models.IntegerField(blank=True, null=True)
    pswd = models.IntegerField(blank=True, null=True)
    regdate = models.DateTimeField(blank=True, null=True)
    pkusage = models.IntegerField(blank=True, null=True)
    mjusage = models.IntegerField(blank=True, null=True)
    evusage = models.IntegerField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    begin1 = models.DateTimeField(blank=True, null=True)
    end1 = models.DateTimeField(blank=True, null=True)
    expired1 = models.BooleanField(blank=True, null=True)
    carnum = models.CharField(max_length=20, blank=True, null=True)
    opname = models.CharField(max_length=20, blank=True, null=True)
    begin2 = models.DateTimeField(blank=True, null=True)
    end2 = models.DateTimeField(blank=True, null=True)
    expired2 = models.IntegerField(blank=True, null=True)
    expbegin = models.DateTimeField(blank=True, null=True)
    expend = models.DateTimeField(blank=True, null=True)
    expired = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_card'


class TbCargate(models.Model):
    autoid = models.AutoField(primary_key=True)
    carnum = models.ForeignKey(TbCar, models.DO_NOTHING, db_column='carnum', blank=True, null=True)
    gateid = models.ForeignKey('TbGate', models.DO_NOTHING, db_column='gateid', blank=True, null=True)
    passmode = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_cargate'


class TbCarlock(models.Model):
    autoid = models.AutoField(primary_key=True)
    datime = models.DateTimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    carnum = models.CharField(max_length=20, blank=True, null=True)
    selflock = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_carlock'


class TbCarpass(models.Model):
    autoid = models.AutoField(primary_key=True)
    time = models.DateTimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    hour = models.IntegerField(blank=True, null=True)
    officeid = models.IntegerField(blank=True, null=True)
    gateid = models.IntegerField(blank=True, null=True)
    gatetype = models.IntegerField(blank=True, null=True)
    in_or_out = models.IntegerField()
    passtype = models.IntegerField(blank=True, null=True)
    n_or_y = models.IntegerField()
    areaid = models.IntegerField(blank=True, null=True)
    exitareaid = models.IntegerField(blank=True, null=True)
    carnum = models.CharField(max_length=20, blank=True, null=True)
    carnumread = models.CharField(max_length=20, blank=True, null=True)
    carattr = models.IntegerField(blank=True, null=True)
    t_or_m = models.IntegerField()
    userid = models.IntegerField(blank=True, null=True)
    cardid = models.IntegerField(blank=True, null=True)
    cardattr = models.IntegerField(blank=True, null=True)
    matchtype = models.IntegerField(blank=True, null=True)
    carsize = models.IntegerField(blank=True, null=True)
    carcolor = models.IntegerField(blank=True, null=True)
    platetype = models.IntegerField(blank=True, null=True)
    platecolor = models.IntegerField(blank=True, null=True)
    inrecid = models.IntegerField(blank=True, null=True)
    payrecid = models.IntegerField(blank=True, null=True)
    intime = models.DateTimeField(blank=True, null=True)
    outime = models.DateTimeField(blank=True, null=True)
    staydays = models.IntegerField(blank=True, null=True)
    stayhours = models.IntegerField(blank=True, null=True)
    stayminutes = models.IntegerField(blank=True, null=True)
    opname = models.CharField(max_length=20, blank=True, null=True)
    dutyid = models.IntegerField(blank=True, null=True)
    zjtype = models.IntegerField(blank=True, null=True)
    zjnum = models.CharField(max_length=30, blank=True, null=True)
    zjpic = models.BinaryField(blank=True, null=True)
    fullpic = models.BinaryField(blank=True, null=True)
    platepic = models.BinaryField(blank=True, null=True)
    envipic = models.BinaryField(blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)
    recogtype = models.IntegerField(blank=True, null=True)
    spared1 = models.IntegerField(blank=True, null=True)
    spared2 = models.IntegerField(blank=True, null=True)
    votetime = models.IntegerField(blank=True, null=True)
    carhide = models.IntegerField(blank=True, null=True)
    picname = models.CharField(max_length=50, blank=True, null=True)
    pictime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_carpass'


class TbCarpay(models.Model):
    autoid = models.AutoField(primary_key=True)
    time = models.DateTimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    hour = models.IntegerField(blank=True, null=True)
    officeid = models.IntegerField(blank=True, null=True)
    officetype = models.IntegerField(blank=True, null=True)
    paytype = models.IntegerField(blank=True, null=True)
    payway = models.IntegerField(blank=True, null=True)
    carnum = models.CharField(max_length=20, blank=True, null=True)
    carattr = models.IntegerField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    cardid = models.IntegerField(blank=True, null=True)
    inrecid = models.IntegerField(blank=True, null=True)
    outrecid = models.IntegerField(blank=True, null=True)
    begindate = models.DateTimeField(blank=True, null=True)
    enddate = models.DateTimeField(blank=True, null=True)
    timefrom = models.DateTimeField(blank=True, null=True)
    timeto = models.DateTimeField(blank=True, null=True)
    staydays = models.IntegerField(blank=True, null=True)
    stayhours = models.IntegerField(blank=True, null=True)
    stayminutes = models.IntegerField(blank=True, null=True)
    dues = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    m_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    t_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    s_cut = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    w_cut = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cutreason = models.CharField(max_length=50, blank=True, null=True)
    refund = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    refundreason = models.CharField(max_length=50, blank=True, null=True)
    dutyid = models.IntegerField(blank=True, null=True)
    opname = models.CharField(max_length=20, blank=True, null=True)
    payee = models.CharField(max_length=50, blank=True, null=True)
    payer = models.CharField(max_length=50, blank=True, null=True)
    payeracc = models.CharField(max_length=50, blank=True, null=True)
    acctype = models.IntegerField(blank=True, null=True)
    paytime = models.DateTimeField(blank=True, null=True)
    payproof1 = models.CharField(max_length=100, blank=True, null=True)
    payproof2 = models.CharField(max_length=100, blank=True, null=True)
    payproof3 = models.CharField(max_length=100, blank=True, null=True)
    carhide = models.IntegerField(blank=True, null=True)
    mpriceid = models.IntegerField(blank=True, null=True)
    tpriceid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_carpay'


class TbCarrefuse(models.Model):
    autoid = models.AutoField(primary_key=True)
    createtime = models.DateTimeField(blank=True, null=True)
    officeid = models.IntegerField(blank=True, null=True)
    gateid = models.IntegerField(blank=True, null=True)
    gatetype = models.IntegerField(blank=True, null=True)
    in_or_out = models.IntegerField()
    carnum = models.CharField(max_length=20, blank=True, null=True)
    carnumread = models.CharField(max_length=20, blank=True, null=True)
    carattr = models.IntegerField(blank=True, null=True)
    t_or_m = models.IntegerField()
    userid = models.IntegerField(blank=True, null=True)
    cardid = models.IntegerField(blank=True, null=True)
    cardattr = models.IntegerField(blank=True, null=True)
    matchtype = models.IntegerField(blank=True, null=True)
    carsize = models.IntegerField(blank=True, null=True)
    carcolor = models.IntegerField(blank=True, null=True)
    platetype = models.IntegerField(blank=True, null=True)
    platecolor = models.IntegerField(blank=True, null=True)
    inrecid = models.IntegerField(blank=True, null=True)
    intime = models.DateTimeField(blank=True, null=True)
    rf_dues = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    staydays = models.IntegerField(blank=True, null=True)
    stayhours = models.IntegerField(blank=True, null=True)
    stayminutes = models.IntegerField(blank=True, null=True)
    opname = models.CharField(max_length=20, blank=True, null=True)
    dutyid = models.IntegerField(blank=True, null=True)
    fullpic = models.BinaryField(blank=True, null=True)
    platepic = models.BinaryField(blank=True, null=True)
    envipic = models.BinaryField(blank=True, null=True)
    recogtype = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_carrefuse'


class TbChatlog(models.Model):
    autoid = models.AutoField(primary_key=True)
    datime = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=20, blank=True, null=True)
    pcname = models.CharField(max_length=20, blank=True, null=True)
    appid = models.IntegerField(blank=True, null=True)
    officeid = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=40, blank=True, null=True)
    opname = models.CharField(max_length=20, blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    toappid = models.IntegerField(blank=True, null=True)
    text = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_chatlog'


class TbDept(models.Model):
    deptid = models.IntegerField(primary_key=True)
    pid = models.IntegerField(blank=True, null=True)
    imgid = models.IntegerField(blank=True, null=True)
    orgstate = models.IntegerField(blank=True, null=True)
    deptcode = models.CharField(max_length=20, blank=True, null=True)
    deptname = models.CharField(max_length=20, blank=True, null=True)
    leader = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=40, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_dept'


class TbDict(models.Model):
    item = models.CharField(primary_key=True, max_length=40)
    value = models.IntegerField()
    caption = models.CharField(max_length=200, blank=True, null=True)
    enabled = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_dict'
        unique_together = (('item', 'value'),)

    def __str__(self):
        return self.caption


class TbGate(models.Model):
    gateid = models.IntegerField(primary_key=True)
    orgstate = models.IntegerField(blank=True, null=True)
    online = models.IntegerField(blank=True, null=True)
    gatename = models.CharField(max_length=20, blank=True, null=True)
    gatetype = models.IntegerField(blank=True, null=True)
    passcheck = models.IntegerField(blank=True, null=True)
    officeid = models.IntegerField(blank=True, null=True)
    mcarpassmode = models.IntegerField(blank=True, null=True)
    tcarpassmode = models.IntegerField(blank=True, null=True)
    areaid = models.IntegerField(blank=True, null=True)
    exitareaid = models.IntegerField(blank=True, null=True)
    platetimeout = models.IntegerField(blank=True, null=True)
    matchignore = models.IntegerField(blank=True, null=True)
    matchsimilar = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)
    passmodetime1 = models.TimeField(blank=True, null=True)
    passmodetime2 = models.TimeField(blank=True, null=True)
    mcarpassmode2 = models.IntegerField(blank=True, null=True)
    tcarpassmode2 = models.IntegerField(blank=True, null=True)
    tickforretire = models.IntegerField(db_column='TickForRetire', blank=True, null=True)  # Field name made lowercase.
    tickforrefreshinfo = models.IntegerField(db_column='TickForRefreshInfo', blank=True, null=True)  # Field name made lowercase.
    tickforreupstrobe = models.IntegerField(db_column='TickForReUpStrobe', blank=True, null=True)  # Field name made lowercase.
    lifeforpass = models.IntegerField(db_column='LifeForPass', blank=True, null=True)  # Field name made lowercase.
    lifeforcharge = models.IntegerField(db_column='LifeForCharge', blank=True, null=True)  # Field name made lowercase.
    lifeforoutercheck = models.IntegerField(db_column='LifeForOuterCheck', blank=True, null=True)  # Field name made lowercase.
    lifeforinnercheck = models.IntegerField(db_column='LifeForInnerCheck', blank=True, null=True)  # Field name made lowercase.
    lifeforrefuse = models.IntegerField(db_column='LifeForRefuse', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_gate'


class TbLog(models.Model):
    autoid = models.AutoField(primary_key=True)
    time = models.DateTimeField(blank=True, null=True)
    pcname = models.CharField(max_length=20, blank=True, null=True)
    pcip = models.CharField(max_length=20, blank=True, null=True)
    appname = models.CharField(max_length=20, blank=True, null=True)
    appid = models.IntegerField(blank=True, null=True)
    opname = models.CharField(max_length=20, blank=True, null=True)
    logtype = models.IntegerField(blank=True, null=True)
    logtext = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_log'


# class TbNoplatepass(models.Model):
#     id = models.AutoField()
#     gateid = models.IntegerField()
#     eventtime = models.DateTimeField(db_column='eventTime', blank=True, null=True)  # Field name made lowercase.
#     isvail = models.IntegerField(blank=True, null=True)
#     type = models.IntegerField()
#     plate = models.CharField(max_length=20, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_noplatepass'


class TbNums(models.Model):
    n = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'tb_nums'


class TbOffice(models.Model):
    officeid = models.IntegerField(primary_key=True)
    orgstate = models.IntegerField(blank=True, null=True)
    officename = models.CharField(max_length=20, blank=True, null=True)
    officetype = models.IntegerField(blank=True, null=True)
    pcname = models.CharField(max_length=20, blank=True, null=True)
    livetime = models.DateTimeField(blank=True, null=True)
    dutyid = models.IntegerField(blank=True, null=True)
    shopcode = models.CharField(max_length=20, blank=True, null=True)
    shoptype = models.IntegerField(blank=True, null=True)
    cuttype = models.IntegerField(blank=True, null=True)
    leader = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    photo = models.BinaryField(blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)
    live = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_office'


class TbOperator(models.Model):
    opname = models.CharField(primary_key=True, max_length=20)
    truename = models.CharField(max_length=20, blank=True, null=True)
    userstate = models.IntegerField(blank=True, null=True)
    optype = models.IntegerField(blank=True, null=True)
    opduty = models.CharField(max_length=20, blank=True, null=True)
    pswd = models.CharField(max_length=10, blank=True, null=True)
    pswdmd5 = models.CharField(max_length=40, blank=True, null=True)
    regdate = models.DateTimeField(blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    zjtype = models.IntegerField(blank=True, null=True)
    zjnum = models.CharField(max_length=30, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    photo = models.BinaryField(blank=True, null=True)
    salt = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)
    readtjpay = models.IntegerField(blank=True, null=True)
    readtjpass = models.IntegerField(blank=True, null=True)
    readscar = models.IntegerField(blank=True, null=True)
    readmcar = models.IntegerField(blank=True, null=True)
    readtcar = models.IntegerField(blank=True, null=True)
    readmcarpay = models.IntegerField(blank=True, null=True)
    readtcarpay = models.IntegerField(blank=True, null=True)
    readycpay = models.IntegerField(blank=True, null=True)
    readmcarpass = models.IntegerField(blank=True, null=True)
    readtcarpass = models.IntegerField(blank=True, null=True)
    readycpass = models.IntegerField(blank=True, null=True)
    readcarpass = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_operator'


# class TbOperight(models.Model):
#     opname = models.ForeignKey(TbOperator, models.DO_NOTHING, db_column='opname', primary_key=True)
#     rightgroup = models.ForeignKey('TbRight', models.DO_NOTHING, db_column='rightgroup')
#     rightitem = models.ForeignKey('TbRight', models.DO_NOTHING, db_column='rightitem')
#     rtread = models.BooleanField(blank=True, null=True)
#     rtwrite = models.BooleanField(blank=True, null=True)
#     rtaudit = models.BooleanField(blank=True, null=True)
#     rightcode = models.CharField(max_length=9, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_operight'
#         unique_together = (('opname'),)


class TbPark(models.Model):
    parkcode = models.CharField(primary_key=True, max_length=20)
    parkname = models.CharField(max_length=40)
    parktype = models.IntegerField(blank=True, null=True)
    orgstate = models.IntegerField(blank=True, null=True)
    regdate = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    contact = models.CharField(max_length=20, blank=True, null=True)
    ip = models.CharField(max_length=20, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    ipupdtime = models.DateTimeField(blank=True, null=True)
    photo = models.BinaryField(blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_park'


class TbParkarea(models.Model):
    areaid = models.AutoField(primary_key=True)
    orgstate = models.IntegerField(blank=True, null=True)
    areaname = models.CharField(max_length=20)
    areatype = models.IntegerField(blank=True, null=True)
    seatcount = models.IntegerField(blank=True, null=True)
    seatused = models.IntegerField(blank=True, null=True)
    seatremain = models.IntegerField(blank=True, null=True)
    seatexist = models.IntegerField(blank=True, null=True)
    seatfull = models.IntegerField(blank=True, null=True)
    usagerate = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_parkarea'


class TbParkduty(models.Model):
    dutyid = models.AutoField(primary_key=True)
    opname = models.CharField(max_length=20, blank=True, null=True)
    officeid = models.IntegerField(blank=True, null=True)
    ontime = models.DateTimeField(blank=True, null=True)
    offtime = models.DateTimeField(blank=True, null=True)
    dutystate = models.IntegerField()
    t_incount = models.IntegerField(blank=True, null=True)
    t_outcount = models.IntegerField(blank=True, null=True)
    m_incount = models.IntegerField(blank=True, null=True)
    m_outcount = models.IntegerField(blank=True, null=True)
    incount = models.IntegerField(blank=True, null=True)
    outcount = models.IntegerField(blank=True, null=True)
    h_incount = models.IntegerField(blank=True, null=True)
    h_outcount = models.IntegerField(blank=True, null=True)
    t_dues = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    t_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    t_cut = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    m_dues = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    m_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    rf_incount = models.IntegerField(blank=True, null=True)
    rf_outcount = models.IntegerField(blank=True, null=True)
    rf_dues = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_parkduty'


class TbParkprice(models.Model):
    priceid = models.IntegerField(primary_key=True)
    orgstate = models.IntegerField(blank=True, null=True)
    pricename = models.CharField(max_length=20, blank=True, null=True)
    defaulted = models.BooleanField(blank=True, null=True)
    pricetype = models.IntegerField(blank=True, null=True)
    carsize = models.IntegerField(blank=True, null=True)
    daytype = models.IntegerField(blank=True, null=True)
    freespan = models.IntegerField(blank=True, null=True)
    freechip = models.IntegerField(blank=True, null=True)
    freeexit = models.IntegerField(blank=True, null=True)
    totalmax = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    countspan = models.IntegerField(blank=True, null=True)
    countprice = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    fstspan = models.IntegerField(blank=True, null=True)
    fstunit = models.IntegerField(blank=True, null=True)
    fstprice = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    unit = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    maxspan = models.IntegerField(blank=True, null=True)
    maxprice = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    daystart = models.TimeField(blank=True, null=True)
    nightstart = models.TimeField(blank=True, null=True)
    d_fstspan = models.IntegerField(blank=True, null=True)
    d_fstunit = models.IntegerField(blank=True, null=True)
    d_fstprice = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    d_unit = models.IntegerField(blank=True, null=True)
    d_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    d_maxprice = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    n_fstspan = models.IntegerField(blank=True, null=True)
    n_fstunit = models.IntegerField(blank=True, null=True)
    n_fstprice = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    n_unit = models.IntegerField(blank=True, null=True)
    n_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    n_maxprice = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)
    yearprice = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    monthprice = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    month3cut = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    month6cut = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    month12cut = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_parkprice'


class TbPicture(models.Model):
    datime = models.DateTimeField()
    type = models.IntegerField(blank=True, null=True)
    picture = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_picture'


class TbPkshopcut(models.Model):
    autoid = models.AutoField(primary_key=True)
    time = models.DateTimeField(blank=True, null=True)
    shopid = models.IntegerField(blank=True, null=True)
    carnum = models.CharField(max_length=20, blank=True, null=True)
    cardid = models.IntegerField(blank=True, null=True)
    cuttype = models.IntegerField(blank=True, null=True)
    cuthours = models.IntegerField(blank=True, null=True)
    cutmoney = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cutrate = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_pkshopcut'


class TbPktask(models.Model):
    autoid = models.AutoField(primary_key=True)
    time = models.DateTimeField()
    cmd = models.IntegerField(blank=True, null=True)
    desttype = models.IntegerField(blank=True, null=True)
    destaddr = models.CharField(max_length=50, blank=True, null=True)
    para1 = models.CharField(max_length=50, blank=True, null=True)
    para2 = models.CharField(max_length=50, blank=True, null=True)
    para3 = models.CharField(max_length=50, blank=True, null=True)
    para4 = models.CharField(max_length=50, blank=True, null=True)
    result = models.IntegerField(blank=True, null=True)
    resulttext = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_pktask'


class TbPlace(models.Model):
    placeid = models.IntegerField(primary_key=True)
    pid = models.IntegerField(blank=True, null=True)
    imgid = models.IntegerField(blank=True, null=True)
    orgstate = models.IntegerField(blank=True, null=True)
    placename = models.CharField(max_length=20, blank=True, null=True)
    placecode = models.CharField(max_length=20, blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_place'


class TbRight(models.Model):
    rightgroup = models.IntegerField(primary_key=True)
    rightitem = models.IntegerField()
    rightname = models.CharField(max_length=40, blank=True, null=True)
    rightcode = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_right'
        unique_together = (('rightgroup', 'rightitem'),)


class TbScreen(models.Model):
    devid = models.IntegerField(primary_key=True)
    gateid = models.IntegerField(blank=True, null=True)
    devstate = models.IntegerField(blank=True, null=True)
    online = models.IntegerField(blank=True, null=True)
    devname = models.CharField(max_length=20, blank=True, null=True)
    screentype = models.IntegerField(blank=True, null=True)
    screenmodel = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=20, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    devcode = models.CharField(max_length=20, blank=True, null=True)
    serialcode = models.CharField(max_length=20, blank=True, null=True)
    activecode = models.CharField(max_length=20, blank=True, null=True)
    activestate = models.IntegerField(blank=True, null=True)
    version = models.CharField(max_length=20, blank=True, null=True)
    scrncolor1 = models.IntegerField(blank=True, null=True)
    scrncolor2 = models.IntegerField(blank=True, null=True)
    scrncolor3 = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)
    time1 = models.TimeField(blank=True, null=True)
    time2 = models.TimeField(blank=True, null=True)
    bright = models.IntegerField(blank=True, null=True)
    bright2 = models.IntegerField(blank=True, null=True)
    color1 = models.IntegerField(blank=True, null=True)
    color2 = models.IntegerField(blank=True, null=True)
    color3 = models.IntegerField(blank=True, null=True)
    color4 = models.IntegerField(blank=True, null=True)
    color5 = models.IntegerField(blank=True, null=True)
    fixed1 = models.IntegerField(blank=True, null=True)
    fixed2 = models.IntegerField(blank=True, null=True)
    fixed3 = models.IntegerField(blank=True, null=True)
    fixed4 = models.IntegerField(blank=True, null=True)
    fixed5 = models.IntegerField(blank=True, null=True)
    text1 = models.CharField(max_length=100, blank=True, null=True)
    text2 = models.CharField(max_length=100, blank=True, null=True)
    text3 = models.CharField(max_length=100, blank=True, null=True)
    text4 = models.CharField(max_length=100, blank=True, null=True)
    text5 = models.CharField(max_length=100, blank=True, null=True)
    pkarea1 = models.IntegerField(blank=True, null=True)
    pkarea2 = models.IntegerField(blank=True, null=True)
    pkarea3 = models.IntegerField(blank=True, null=True)
    pkarea4 = models.IntegerField(blank=True, null=True)
    pkarea5 = models.IntegerField(blank=True, null=True)
    staytime1 = models.IntegerField(blank=True, null=True)
    staytime2 = models.IntegerField(blank=True, null=True)
    staytime3 = models.IntegerField(blank=True, null=True)
    staytime4 = models.IntegerField(blank=True, null=True)
    staytime5 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_screen'


class TbScreentype(models.Model):
    screentype = models.IntegerField(db_column='ScreenType', primary_key=True)  # Field name made lowercase.
    screenname = models.CharField(db_column='ScreenName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    width = models.IntegerField(db_column='Width', blank=True, null=True)  # Field name made lowercase.
    height = models.IntegerField(db_column='Height', blank=True, null=True)  # Field name made lowercase.
    areacount = models.IntegerField(db_column='AreaCount', blank=True, null=True)  # Field name made lowercase.
    top1 = models.IntegerField(blank=True, null=True)
    top2 = models.IntegerField(blank=True, null=True)
    top3 = models.IntegerField(blank=True, null=True)
    top4 = models.IntegerField(blank=True, null=True)
    top5 = models.IntegerField(blank=True, null=True)
    height1 = models.IntegerField(db_column='Height1', blank=True, null=True)  # Field name made lowercase.
    height2 = models.IntegerField(db_column='Height2', blank=True, null=True)  # Field name made lowercase.
    height3 = models.IntegerField(db_column='Height3', blank=True, null=True)  # Field name made lowercase.
    height4 = models.IntegerField(db_column='Height4', blank=True, null=True)  # Field name made lowercase.
    height5 = models.IntegerField(db_column='Height5', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_screentype'


class TbSpk(models.Model):
    devid = models.IntegerField(primary_key=True)
    gateid = models.IntegerField(blank=True, null=True)
    devstate = models.IntegerField(blank=True, null=True)
    online = models.IntegerField(blank=True, null=True)
    devname = models.CharField(max_length=20, blank=True, null=True)
    spktype = models.IntegerField(blank=True, null=True)
    spkmodel = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=20, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    devcode = models.CharField(max_length=20, blank=True, null=True)
    serialcode = models.CharField(max_length=20, blank=True, null=True)
    activecode = models.CharField(max_length=20, blank=True, null=True)
    activestate = models.IntegerField(blank=True, null=True)
    version = models.CharField(max_length=20, blank=True, null=True)
    announcer = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)
    time1 = models.TimeField(blank=True, null=True)
    time2 = models.TimeField(blank=True, null=True)
    volume2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_spk'


class TbStrobe(models.Model):
    devid = models.IntegerField(primary_key=True)
    gateid = models.IntegerField(blank=True, null=True)
    devstate = models.IntegerField(blank=True, null=True)
    online = models.IntegerField(blank=True, null=True)
    devname = models.CharField(max_length=20, blank=True, null=True)
    strobetype = models.IntegerField(blank=True, null=True)
    strobemodel = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=20, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    areaid = models.IntegerField(blank=True, null=True)
    rail = models.IntegerField(blank=True, null=True)
    devcode = models.CharField(max_length=20, blank=True, null=True)
    serialcode = models.CharField(max_length=20, blank=True, null=True)
    activecode = models.CharField(max_length=20, blank=True, null=True)
    activestate = models.IntegerField(blank=True, null=True)
    version = models.CharField(max_length=20, blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_strobe'


class TbSysref(models.Model):
    refname = models.CharField(primary_key=True, max_length=50)
    refvalue = models.CharField(max_length=200, blank=True, null=True)
    refbin = models.BinaryField(blank=True, null=True)
    refdatime = models.DateTimeField(blank=True, null=True)
    caption = models.CharField(max_length=200, blank=True, null=True)
    groupid = models.IntegerField(blank=True, null=True)
    seqid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_sysref'


# class TbTest(models.Model):
#     id = models.IntegerField(blank=True, null=True)
#     value = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_test'


class TbUser(models.Model):
    userid = models.AutoField(primary_key=True)
    userstate = models.IntegerField(blank=True, null=True)
    usertype = models.IntegerField(blank=True, null=True)
    usercode = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    zjtype = models.IntegerField(blank=True, null=True)
    zjnum = models.CharField(max_length=30, blank=True, null=True)
    zjaddress = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    deptid = models.IntegerField(blank=True, null=True)
    placeid = models.IntegerField(blank=True, null=True)
    workunit = models.CharField(max_length=40, blank=True, null=True)
    job = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)
    photo = models.BinaryField(blank=True, null=True)
    regdate = models.DateTimeField(blank=True, null=True)
    netsigned = models.BooleanField(blank=True, null=True)
    netsignedate = models.DateTimeField(blank=True, null=True)
    netname = models.CharField(max_length=20, blank=True, null=True)
    netpswd = models.CharField(max_length=8, blank=True, null=True)
    netprompt = models.CharField(max_length=20, blank=True, null=True)
    netquestion = models.CharField(max_length=40, blank=True, null=True)
    netanswer = models.CharField(max_length=20, blank=True, null=True)
    borthdate = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)
    opname = models.CharField(max_length=20, blank=True, null=True)

    # dict = models.ManyToManyField('TbDict', null=True)  #多表联合查询需要加这个字段
    class Meta:
        managed = False
        db_table = 'tb_user'


class TjPkareaday(models.Model):
    autoid = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    areaid = models.IntegerField(blank=True, null=True)
    incount = models.IntegerField(blank=True, null=True)
    outcount = models.IntegerField(blank=True, null=True)
    added = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tj_pkareaday'


class TjPkareahour(models.Model):
    autoid = models.AutoField(primary_key=True)
    datime = models.DateTimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    hour = models.IntegerField(blank=True, null=True)
    areaid = models.IntegerField(blank=True, null=True)
    seatcount = models.IntegerField(blank=True, null=True)
    seatused = models.IntegerField(blank=True, null=True)
    usagerate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tj_pkareahour'


class TjPkdaypass(models.Model):
    autoid = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    gateid = models.IntegerField(blank=True, null=True)
    gatetype = models.IntegerField(blank=True, null=True)
    t_in = models.IntegerField(blank=True, null=True)
    m_in = models.IntegerField(blank=True, null=True)
    incount = models.IntegerField(blank=True, null=True)
    t_out = models.IntegerField(blank=True, null=True)
    m_out = models.IntegerField(blank=True, null=True)
    outcount = models.IntegerField(blank=True, null=True)
    y_count = models.IntegerField(blank=True, null=True)
    t_count = models.IntegerField(blank=True, null=True)
    m_count = models.IntegerField(blank=True, null=True)
    counts = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tj_pkdaypass'


class TjPkdaypay(models.Model):
    autoid = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    officeid = models.IntegerField(blank=True, null=True)
    officetype = models.IntegerField(blank=True, null=True)
    t_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    m_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    s_cut = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    w_cut = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    refund = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    paid_count = models.IntegerField(blank=True, null=True)
    cash_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    bank_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    shop_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    weixin_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    alipay_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tj_pkdaypay'


class TjPkhourpass(models.Model):
    autoid = models.AutoField(primary_key=True)
    datime = models.DateTimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    hour = models.IntegerField(blank=True, null=True)
    gateid = models.IntegerField(blank=True, null=True)
    gatetype = models.IntegerField(blank=True, null=True)
    t_in = models.IntegerField(blank=True, null=True)
    m_in = models.IntegerField(blank=True, null=True)
    t_out = models.IntegerField(blank=True, null=True)
    m_out = models.IntegerField(blank=True, null=True)
    y_count = models.IntegerField(blank=True, null=True)
    incount = models.IntegerField(blank=True, null=True)
    outcount = models.IntegerField(blank=True, null=True)
    t_count = models.IntegerField(blank=True, null=True)
    m_count = models.IntegerField(blank=True, null=True)
    counts = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tj_pkhourpass'


class TjPkhourpay(models.Model):
    autoid = models.AutoField(primary_key=True)
    datime = models.DateTimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    hour = models.IntegerField(blank=True, null=True)
    officeid = models.IntegerField(blank=True, null=True)
    officetype = models.IntegerField(blank=True, null=True)
    t_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    m_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    s_cut = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    w_cut = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    refund = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    paid_count = models.IntegerField(blank=True, null=True)
    cash_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    bank_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    shop_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    weixin_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    alipay_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tj_pkhourpay'


class TjPkmonthpass(models.Model):
    autoid = models.AutoField(primary_key=True)
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    monthid = models.IntegerField(blank=True, null=True)
    yearmonth = models.CharField(max_length=13, blank=True, null=True)
    gateid = models.IntegerField(blank=True, null=True)
    gatetype = models.IntegerField(blank=True, null=True)
    t_in = models.IntegerField(blank=True, null=True)
    m_in = models.IntegerField(blank=True, null=True)
    incount = models.IntegerField(blank=True, null=True)
    t_out = models.IntegerField(blank=True, null=True)
    m_out = models.IntegerField(blank=True, null=True)
    outcount = models.IntegerField(blank=True, null=True)
    y_count = models.IntegerField(blank=True, null=True)
    t_count = models.IntegerField(blank=True, null=True)
    m_count = models.IntegerField(blank=True, null=True)
    counts = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tj_pkmonthpass'


class TjPkmonthpay(models.Model):
    autoid = models.AutoField(primary_key=True)
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    monthid = models.IntegerField(blank=True, null=True)
    yearmonth = models.CharField(max_length=13, blank=True, null=True)
    officeid = models.IntegerField(blank=True, null=True)
    officetype = models.IntegerField(blank=True, null=True)
    t_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    m_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    s_cut = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    w_cut = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    refund = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    paid_count = models.IntegerField(blank=True, null=True)
    cash_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    bank_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    shop_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    weixin_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    alipay_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tj_pkmonthpay'


class TjPkyearpass(models.Model):
    autoid = models.AutoField(primary_key=True)
    year = models.IntegerField(blank=True, null=True)
    gateid = models.IntegerField(blank=True, null=True)
    gatetype = models.IntegerField(blank=True, null=True)
    t_in = models.IntegerField(blank=True, null=True)
    m_in = models.IntegerField(blank=True, null=True)
    incount = models.IntegerField(blank=True, null=True)
    t_out = models.IntegerField(blank=True, null=True)
    m_out = models.IntegerField(blank=True, null=True)
    outcount = models.IntegerField(blank=True, null=True)
    y_count = models.IntegerField(blank=True, null=True)
    t_count = models.IntegerField(blank=True, null=True)
    m_count = models.IntegerField(blank=True, null=True)
    counts = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tj_pkyearpass'


class TjPkyearpay(models.Model):
    autoid = models.AutoField(primary_key=True)
    year = models.IntegerField(blank=True, null=True)
    officeid = models.IntegerField(blank=True, null=True)
    officetype = models.IntegerField(blank=True, null=True)
    t_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    m_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    s_cut = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    w_cut = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    refund = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    paid_count = models.IntegerField(blank=True, null=True)
    cash_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    bank_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    shop_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    weixin_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    alipay_paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tj_pkyearpay'


class Addpath(models.Model):  #楼栋数据库的视图model
    placeid = models.IntegerField(primary_key=True)
    nest = models.IntegerField(blank=True, null=True)
    pathid = models.IntegerField(blank=True, null=True)
    pathname = models.CharField(max_length=100)

    class Meta:
        db_table = 'vw_placepath'

