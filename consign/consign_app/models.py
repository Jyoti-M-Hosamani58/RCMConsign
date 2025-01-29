from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50,null=True)
    utype = models.CharField(max_length=50)

class Branch(models.Model):
    headname = models.CharField(max_length=150, null=True)
    companyname = models.CharField(max_length=50, null=True)
    phonenumber = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    gst = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    prefix = models.CharField(max_length=50, null=True)
    branchtype = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=50, null=True)
    branchcode = models.CharField(max_length=50, null=True)



class AddConsignment(models.Model):
    track_id = models.CharField(max_length=200,null=True)
    sender_name = models.CharField(max_length=50, null=True)
    sender_mobile = models.CharField(max_length=50, null=True)
    sender_email = models.CharField(max_length=50, null=True)
    sender_address = models.CharField(max_length=50, null=True)
    sender_GST=models.CharField(max_length=50,null=True)
    receiver_name = models.CharField(max_length=50, null=True)
    receiver_mobile = models.CharField(max_length=50, null=True)
    receiver_email = models.CharField(max_length=50, null=True)
    receiver_address = models.CharField(max_length=50, null=True)
    receiver_GST = models.CharField(max_length=50, null=True)
    total_cost = models.FloatField(null=True)
    date = models.DateField(max_length=30, null=True)
    pay_status = models.CharField(max_length=30, null=True)
    pay_type = models.CharField(max_length=30, null=True)
    pay_tbb = models.CharField(max_length=30, null=True)
    pay_method = models.CharField(max_length=30, null=True)
    route_from = models.CharField(max_length=30, null=True)
    route_to = models.CharField(max_length=30, null=True)
    invoiceNo = models.CharField(max_length=50,null=True)
    invoicevalue = models.CharField(max_length=50,null=True)
    actualweight = models.FloatField(null=True)
    invoiceeway = models.CharField(max_length=150, null=True)
    paidweight = models.FloatField(null=True)
    freight = models.FloatField(null=True)
    hamali = models.FloatField(null=True)
    delivery_charge = models.FloatField(null=True)
    collection_charge = models.FloatField(null=True)
    st_charge = models.FloatField(null=True)
    Consignment_id=models.IntegerField(null=True)
    branch = models.CharField(max_length=150, null=True)
    branchcode = models.CharField(max_length=150, null=True)
    name = models.CharField(max_length=150, null=True)
    otherCharge = models.FloatField(null=True)
    time=models.CharField(max_length=50,null=True)
    copy_type = models.CharField(max_length=150, null=True)
    collection_type = models.CharField(max_length=150, null=True)
    weightAmt=models.FloatField(null=True)
    collection_type = models.CharField(max_length=150, null=True)
    branchemail = models.CharField(max_length=150, null=True)
    delivery_type = models.CharField(max_length=150,null=True)
    accountHolder = models.CharField(max_length=150,null=True)
    deduction = models.FloatField(max_length=150, null=True)
    dcno = models.CharField(max_length=150, null=True)
    dcvalue = models.CharField(max_length=150, null=True)
    dcewaybill = models.CharField(max_length=150, null=True)
    loadtype = models.CharField(max_length=150, null=True)
    invoiceType = models.CharField(max_length=150, null=True)
    dc = models.CharField(max_length=150, null=True)
    invoice = models.CharField(max_length=150, null=True)
    totalpieces = models.CharField(max_length=150, null=True)
    totalactalweight = models.CharField(max_length=150, null=True)
    totalpaidweight = models.CharField(max_length=150, null=True)
    collectionVehicleNo = models.CharField(max_length=150, null=True)
    collectionLocation = models.CharField(max_length=150, null=True)
    remark = models.CharField(max_length=500, null=True)
    codapplicable = models.CharField(max_length=500, null=True)
    gstapplicable = models.CharField(max_length=500, null=True)
    fov = models.FloatField(null=True)
    cod = models.FloatField(null=True)
    gstcharge = models.FloatField(null=True)
    pkgcharge = models.FloatField(null=True)
    actualweightvalue=models.FloatField(null=True)
    paidweightvalue=models.FloatField(null=True)
    desc_product = models.CharField(max_length=150, null=True)
    prodDesc = models.CharField(max_length=150, null=True)
    pieces = models.IntegerField(null=True)
    actualweight = models.FloatField(max_length=150, null=True)
    paidweight = models.FloatField(max_length=150, null=True)
    gcType = models.CharField(max_length=150, null=True)
    thirdPartyName = models.CharField(max_length=150, null=True)
    thirdPartyId = models.IntegerField(max_length=150, null=True)
    tbbAt = models.CharField(max_length=150, null=True)



    def __str__(self):
        return self.track_id

class AddConsignmentTemp(models.Model):
    track_id = models.CharField(max_length=200,null=True)
    sender_name = models.CharField(max_length=50, null=True)
    sender_mobile = models.CharField(max_length=50, null=True)
    sender_email = models.CharField(max_length=50, null=True)
    sender_address = models.CharField(max_length=50, null=True)
    sender_GST=models.CharField(max_length=50,null=True)
    receiver_name = models.CharField(max_length=50, null=True)
    receiver_email = models.CharField(max_length=50, null=True)
    receiver_mobile = models.CharField(max_length=50, null=True)
    receiver_address = models.CharField(max_length=50, null=True)
    receiver_GST = models.CharField(max_length=50, null=True)
    total_cost = models.FloatField(null=True)
    date = models.DateField( null=True)
    pay_status = models.CharField(max_length=30, null=True)
    pay_method = models.CharField(max_length=30, null=True)
    route_from = models.CharField(max_length=30, null=True)
    route_to = models.CharField(max_length=30, null=True)
    invoiceNo = models.CharField(max_length=50, null=True)
    invoicevalue = models.CharField(max_length=50, null=True)
    invoiceeway = models.CharField(max_length=150, null=True)
    weight = models.FloatField(null=True)
    freight = models.FloatField(null=True)
    hamali = models.FloatField(null=True)
    door_charge = models.FloatField(null=True)
    st_charge = models.FloatField(null=True)
    Consignment_id=models.IntegerField(null=True)
    branch = models.CharField(max_length=150, null=True)
    branchcode = models.CharField(max_length=150, null=True)
    name = models.CharField(max_length=150, null=True)
    otherCharge = models.FloatField(null=True)
    time = models.CharField(max_length=50,null=True)
    copy_type = models.CharField(max_length=150,null=True)
    delivery_type = models.CharField(max_length=150,null=True)
    weightAmt = models.FloatField(null=True)
    branchemail = models.CharField(max_length=150, null=True)
    actualweight = models.FloatField(max_length=150, null=True)
    dcno = models.CharField(max_length=150, null=True)
    dcvalue = models.CharField(max_length=150, null=True)
    dcewaybill = models.CharField(max_length=150, null=True)
    loadtype = models.CharField(max_length=150, null=True)
    invoiceType = models.CharField(max_length=150, null=True)
    dc = models.CharField(max_length=150, null=True)
    invoice = models.CharField(max_length=150, null=True)
    totalpieces = models.CharField(max_length=150, null=True)
    totalactalweight = models.CharField(max_length=150, null=True)
    totalpaidweight = models.CharField(max_length=150, null=True)
    accountHolder = models.CharField(max_length=150,null=True)
    collectionVehicleNo = models.CharField(max_length=150, null=True)
    collectionLocation = models.CharField(max_length=150, null=True)
    remark = models.CharField(max_length=500, null=True)
    codapplicable = models.CharField(max_length=500, null=True)
    gstapplicable = models.CharField(max_length=500, null=True)
    fov = models.FloatField(null=True)
    cod = models.FloatField(null=True)
    gstcharge = models.FloatField(null=True)
    pkgcharge = models.FloatField(null=True)
    actualweightvalue = models.FloatField(null=True)
    paidweightvalue = models.FloatField(null=True)
    desc_product = models.CharField(max_length=150, null=True)
    prodDesc = models.CharField(max_length=150, null=True)
    pieces = models.IntegerField(null=True)
    actualweight = models.FloatField(max_length=150, null=True)
    paidweight = models.FloatField(max_length=150, null=True)
    deduction = models.FloatField(max_length=150, null=True)
    delivery_charge = models.FloatField(null=True)
    collection_charge = models.FloatField(null=True)
    collection_type = models.CharField(max_length=150, null=True)
    pay_tbb = models.CharField(max_length=30, null=True)
    gcType = models.CharField(max_length=150, null=True)
    thirdPartyName = models.CharField(max_length=150, null=True)
    thirdPartyId = models.IntegerField(max_length=150, null=True)
    tbbAt = models.CharField(max_length=150, null=True)



class Consignor(models.Model):
    sender_name = models.CharField(max_length=50, null=True)
    sender_mobile = models.CharField(max_length=50, null=True)
    sender_email = models.CharField(max_length=50, null=True)
    sender_address = models.CharField(max_length=50, null=True)
    sender_city = models.CharField(max_length=50, null=True)
    sender_pincode = models.CharField(max_length=50, null=True)
    sender_pickup = models.CharField(max_length=50, null=True)
    sender_foc = models.CharField(max_length=50, null=True)
    sender_tbb = models.CharField(max_length=50, null=True)
    sender_company=models.CharField(max_length=50,null=True)
    sender_GST=models.CharField(max_length=50,null=True)
    sender_GSTApplicable=models.CharField(max_length=50,null=True)
    branch=models.CharField(max_length=50,null=True)



class Consignee(models.Model):
    receiver_name = models.CharField(max_length=50, null=True)
    receiver_mobile = models.CharField(max_length=50, null=True)
    receiver_email = models.CharField(max_length=50, null=True)
    receiver_address = models.CharField(max_length=50, null=True)
    receiver_city = models.CharField(max_length=50, null=True)
    receiver_pincode = models.CharField(max_length=50, null=True)
    receiver_pickup = models.CharField(max_length=50, null=True)
    receiver_tbb = models.CharField(max_length=50, null=True)
    receiver_foc = models.CharField(max_length=50, null=True)
    receiver_company = models.CharField(max_length=50, null=True)
    receiver_GST = models.CharField(max_length=50, null=True)
    receiver_GSTApplicable = models.CharField(max_length=50, null=True)
    branch=models.CharField(max_length=50,null=True)

class Client(models.Model):
    name = models.CharField(max_length=500, null=True)
    mobile = models.CharField(max_length=500, null=True)
    telephone = models.CharField(max_length=500, null=True)
    email = models.CharField(max_length=500, null=True)
    address = models.CharField(max_length=500, null=True)
    city = models.CharField(max_length=500, null=True)
    pincode = models.CharField(max_length=500, null=True)
    pickup = models.CharField(max_length=500, null=True)
    tbb = models.CharField(max_length=500, null=True)
    foc = models.CharField(max_length=500, null=True)
    GST = models.CharField(max_length=500, null=True)
    clientType = models.CharField(max_length=500, null=True)
    thirdParty = models.CharField(max_length=500, null=True)

class Incharge(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE,null=True)
    inchargeName = models.CharField(max_length=500, null=True)
    inchargePhone = models.IntegerField(null=True)
    inchargeRole = models.CharField(max_length=500, null=True)
    inchargeEmail = models.CharField(max_length=500, null=True)

class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=50, null=True)
    rccard = models.ImageField(max_length=50, null=True)
    rccardate = models.DateField(null=True)
    incurence = models.ImageField(max_length=50, null=True)
    incurencedate = models.DateField(null=True)
    permit = models.ImageField(max_length=50, null=True)
    permitdate = models.DateField(null=True)
    tax = models.ImageField(max_length=50, null=True)
    taxdate = models.DateField(null=True)
    emission = models.ImageField(max_length=50, null=True)
    emissiondate = models.DateField(null=True)


class Driver(models.Model):
    driver_name = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    passport = models.ImageField(max_length=50, null=True)
    license = models.ImageField(max_length=50, null=True)
    aadhar = models.ImageField(max_length=50, null=True)


class Location(models.Model):
    latitude = models.CharField(max_length=150,null=True)
    longitude =models.CharField(max_length=150,null=True)
    city = models.CharField(max_length=150,null=True)
    created_at = models.DateTimeField(null=True)

class Staff(models.Model):
    staffname = models.CharField(max_length=150, null=True)
    staffPhone = models.CharField(max_length=150, null=True)
    staffaddress = models.CharField(max_length=150, null=True)
    aadhar = models.CharField(max_length=150, null=True)
    staffid = models.CharField(max_length=150, null=True)
    Branch = models.CharField(max_length=150, null=True)
    passbook = models.CharField(max_length=150, null=True)
    passbookphoto = models.CharField(max_length=150, null=True)
    passport = models.CharField(max_length=150, null=True)
    branchemail = models.CharField(max_length=150, null=True)

class Expenses(models.Model):
    Date=models.DateField(null=True)
    Reason=models.CharField(max_length=150,null=True)
    Amount=models.CharField(max_length=150,null=True)
    branch=models.CharField(max_length=150,null=True)
    username=models.CharField(max_length=150,null=True)
    staffname = models.CharField(max_length=150, null=True)

class Disel(models.Model):
    Date = models.CharField(max_length=50, null=True)
    vehicalno = models.CharField(max_length=50, null=True)
    drivername = models.CharField(max_length=50, null=True)
    ltrate = models.FloatField(max_length=50, null=True)
    liter = models.FloatField(max_length=50, null=True)
    total = models.FloatField(max_length=50, null=True)
    trip_id = models.FloatField(max_length=50, null=True)

class Vendor(models.Model):
    companyname = models.CharField(max_length=500, null=True)
    phone = models.IntegerField(null=True)
    address = models.CharField(max_length=500, null=True)
    gst = models.CharField(max_length=500, null=True)
    vehicleNo = models.CharField(max_length=500, null=True)
    renewaldate = models.CharField(max_length=500, null=True)
    document = models.FileField(upload_to='documents/', null=True, blank=True)  # PDF storage
    vehicledocument = models.FileField(upload_to='vehicledocuments/', null=True, blank=True)  # PDF storage
    vehiclerenewaldate = models.CharField(max_length=500, null=True)

class Account(models.Model):
    Date = models.CharField(max_length=50, null=True)
    track_number = models.CharField(max_length=50)
    debit = models.CharField(max_length=50, null=True)
    credit = models.CharField(max_length=50, null=True)
    Balance = models.CharField(max_length=50, null=True)
    sender_name = models.CharField(max_length=255)
    sender_name = models.CharField(max_length=255)
    TrType = models.CharField(max_length=50, null=True)
    particulars = models.CharField(max_length=50, null=True)
    headname = models.CharField(max_length=50, null=True)
    Branch=models.CharField(max_length=150,null=True)

class LHSPrem(models.Model):
    DriverName=models.CharField(max_length=150,null=True)
    DriverNumber=models.CharField(max_length=150,null=True)
    VehicalNo=models.CharField(max_length=150,null=True)
    AdvGiven=models.CharField(max_length=150,null=True)
    DLNo=models.CharField(max_length=150,null=True)
    ownerName=models.CharField(max_length=150,null=True)
    route_from=models.CharField(max_length=150,null=True)
    route_to=models.CharField(max_length=150,null=True)
    countGC=models.IntegerField(null=True)
    paidWeight=models.FloatField(null=True)
    weight=models.FloatField(null=True)
    Time=models.TimeField(null=True)
    Date=models.DateField(null=True)
    LTRate=models.FloatField(null=True)
    Ltr=models.FloatField(null=True)
    LRno=models.IntegerField(null=True)
    qty=models.IntegerField(null=True)
    desc=models.CharField(max_length=150,null=True)
    dest=models.CharField(max_length=150,null=True)
    consignee=models.CharField(max_length=150,null=True)
    username=models.CharField(max_length=150,null=True)
    pay_status = models.CharField(max_length=150, null=True)
    branch=models.CharField(max_length=150,null=True)
    total_cost = models.FloatField(null=True)
    freight = models.FloatField(null=True)
    hamali = models.FloatField(null=True)
    st_charge = models.FloatField(null=True)
    door_charge = models.FloatField(null=True)
    trip_id =models.CharField(max_length=150,null=True)
    status =models.CharField(max_length=150,null=True)
    weightAmt = models.IntegerField(null=True)



class LHSTemp(models.Model):
    Date=models.DateField(null=True)
    LRno=models.IntegerField(null=True)
    qty=models.IntegerField(null=True)
    desc=models.CharField(max_length=150,null=True)
    dest=models.CharField(max_length=150,null=True)
    consignee=models.CharField(max_length=150,null=True)
    username=models.CharField(max_length=150,null=True)
    pay_status = models.CharField(max_length=150, null=True)
    branch = models.CharField(max_length=150, null=True)
    total_cost=models.FloatField( null=True)
    freight = models.FloatField(null=True)
    hamali = models.FloatField(null=True)
    st_charge = models.FloatField(null=True)
    door_charge = models.FloatField(null=True)
    weightAmt = models.FloatField(null=True)
    weight = models.FloatField(null=True)


class GDMTemp(models.Model):
    DriverName=models.CharField(max_length=150,null=True)
    DriverNumber=models.CharField(max_length=150,null=True)
    VehicalNo=models.CharField(max_length=150,null=True)
    AdvGiven=models.CharField(max_length=150,null=True)
    DLNo=models.CharField(max_length=150,null=True)
    ownerName=models.CharField(max_length=150,null=True)
    route_from=models.CharField(max_length=150,null=True)
    route_to=models.CharField(max_length=150,null=True)
    countGC=models.IntegerField(null=True)
    paidWeight=models.FloatField(null=True)
    weight=models.FloatField(null=True)
    Time=models.TimeField(null=True)
    Date=models.DateField(null=True)
    LTRate=models.FloatField(null=True)
    Ltr=models.FloatField(null=True)
    LRno=models.IntegerField(null=True)
    qty=models.IntegerField(null=True)
    desc=models.CharField(max_length=150,null=True)
    dest=models.CharField(max_length=150,null=True)
    consignee=models.CharField(max_length=150,null=True)
    username=models.CharField(max_length=150,null=True)
    pay_status = models.CharField(max_length=150, null=True)
    branch=models.CharField(max_length=150,null=True)
    total_cost = models.FloatField(null=True)
    freight = models.FloatField(null=True)
    hamali = models.FloatField(null=True)
    st_charge = models.FloatField(null=True)
    door_charge = models.FloatField(null=True)
    trip_id =models.CharField(max_length=150,null=True)
    status =models.CharField(max_length=150,null=True)
    weightAmt = models.IntegerField(null=True)

class GDMPrem(models.Model):
    DriverName=models.CharField(max_length=150,null=True)
    DriverNumber=models.CharField(max_length=150,null=True)
    VehicalNo=models.CharField(max_length=150,null=True)
    AdvGiven=models.CharField(max_length=150,null=True)
    DLNo=models.CharField(max_length=150,null=True)
    ownerName=models.CharField(max_length=150,null=True)
    route_from=models.CharField(max_length=150,null=True)
    route_to=models.CharField(max_length=150,null=True)
    countGC=models.IntegerField(null=True)
    paidWeight=models.FloatField(null=True)
    weight=models.FloatField(null=True)
    Time=models.TimeField(null=True)
    Date=models.DateField(null=True)
    LTRate=models.FloatField(null=True)
    Ltr=models.FloatField(null=True)
    LRno=models.IntegerField(null=True)
    qty=models.IntegerField(null=True)
    desc=models.CharField(max_length=150,null=True)
    dest=models.CharField(max_length=150,null=True)
    consignee=models.CharField(max_length=150,null=True)
    username=models.CharField(max_length=150,null=True)
    pay_status = models.CharField(max_length=150, null=True)
    branch=models.CharField(max_length=150,null=True)
    total_cost = models.FloatField(null=True)
    freight = models.FloatField(null=True)
    hamali = models.FloatField(null=True)
    st_charge = models.FloatField(null=True)
    door_charge = models.FloatField(null=True)
    trip_id =models.CharField(max_length=150,null=True)
    status =models.CharField(max_length=150,null=True)
    weightAmt = models.IntegerField(null=True)

class TURTemp(models.Model):
    DriverName=models.CharField(max_length=150,null=True)
    DriverNumber=models.CharField(max_length=150,null=True)
    VehicalNo=models.CharField(max_length=150,null=True)
    AdvGiven=models.CharField(max_length=150,null=True)
    DLNo=models.CharField(max_length=150,null=True)
    ownerName=models.CharField(max_length=150,null=True)
    route_from=models.CharField(max_length=150,null=True)
    route_to=models.CharField(max_length=150,null=True)
    countGC=models.IntegerField(null=True)
    paidWeight=models.FloatField(null=True)
    weight=models.FloatField(null=True)
    Time=models.TimeField(null=True)
    Date=models.DateField(null=True)
    LTRate=models.FloatField(null=True)
    Ltr=models.FloatField(null=True)
    LRno=models.IntegerField(null=True)
    qty=models.IntegerField(null=True)
    desc=models.CharField(max_length=150,null=True)
    dest=models.CharField(max_length=150,null=True)
    consignee=models.CharField(max_length=150,null=True)
    username=models.CharField(max_length=150,null=True)
    pay_status = models.CharField(max_length=150, null=True)
    branch=models.CharField(max_length=150,null=True)
    total_cost = models.FloatField(null=True)
    freight = models.FloatField(null=True)
    hamali = models.FloatField(null=True)
    st_charge = models.FloatField(null=True)
    door_charge = models.FloatField(null=True)
    trip_id =models.CharField(max_length=150,null=True)
    status =models.CharField(max_length=150,null=True)
    weightAmt = models.IntegerField(null=True)

class TURPrem(models.Model):
    DriverName=models.CharField(max_length=150,null=True)
    DriverNumber=models.CharField(max_length=150,null=True)
    VehicalNo=models.CharField(max_length=150,null=True)
    AdvGiven=models.CharField(max_length=150,null=True)
    DLNo=models.CharField(max_length=150,null=True)
    ownerName=models.CharField(max_length=150,null=True)
    route_from=models.CharField(max_length=150,null=True)
    route_to=models.CharField(max_length=150,null=True)
    countGC=models.IntegerField(null=True)
    paidWeight=models.FloatField(null=True)
    weight=models.FloatField(null=True)
    Time=models.TimeField(null=True)
    Date=models.DateField(null=True)
    LTRate=models.FloatField(null=True)
    Ltr=models.FloatField(null=True)
    LRno=models.IntegerField(null=True)
    qty=models.IntegerField(null=True)
    desc=models.CharField(max_length=150,null=True)
    dest=models.CharField(max_length=150,null=True)
    consignee=models.CharField(max_length=150,null=True)
    username=models.CharField(max_length=150,null=True)
    pay_status = models.CharField(max_length=150, null=True)
    branch=models.CharField(max_length=150,null=True)
    total_cost = models.FloatField(null=True)
    freight = models.FloatField(null=True)
    hamali = models.FloatField(null=True)
    st_charge = models.FloatField(null=True)
    door_charge = models.FloatField(null=True)
    trip_id =models.CharField(max_length=150,null=True)
    status =models.CharField(max_length=150,null=True)
    weightAmt = models.IntegerField(null=True)

class TBBRate(models.Model):
    tbbName = models.CharField(max_length=500,null=True)
    tbbId = models.IntegerField(null=True)
    route_from = models.CharField(max_length=500,null=True)
    route_to = models.CharField(max_length=500, null=True)
    rate = models.FloatField(null=True)
    doorCollection = models.FloatField(null=True)
    doorDelivery = models.FloatField(null=True)
    cod = models.FloatField(null=True)

class Rate(models.Model):
    route_from = models.CharField(max_length=500,null=True)
    route_to = models.CharField(max_length=500, null=True)
    rate = models.FloatField(null=True)
    doorCollection = models.FloatField(null=True)
    doorDelivery = models.FloatField(null=True)
    cod = models.FloatField(null=True)

class Pickcharge(models.Model):
    pickPlace = models.CharField(max_length=500,null=True)
    pickrate = models.FloatField(null=True)

class Delcharge(models.Model):
    delPlace = models.CharField(max_length=500,null=True)
    delrate = models.FloatField(null=True)

class CorPickcharge(models.Model):
    clientName = models.CharField(max_length=500,null=True)
    pickPlace = models.CharField(max_length=500,null=True)
    clientId = models.IntegerField(null=True)
    pickrate = models.FloatField(null=True)

class CorDelcharge(models.Model):
    clientName = models.CharField(max_length=500, null=True)
    clientId = models.IntegerField(null=True)
    delPlace = models.CharField(max_length=500,null=True)
    delrate = models.FloatField(null=True)

class LCMTemp(models.Model):
    consignment = models.ForeignKey(AddConsignment, on_delete=models.CASCADE,null=True)
    collection_type = models.CharField(max_length=255, null=True)
    collectionLocation = models.CharField(max_length=255, null=True)
    collectionVehicleNo = models.CharField(max_length=255, null=True)
    branch = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    branchemail = models.CharField(max_length=255, null=True)
    track_id = models.CharField(max_length=50, blank=True, null=True)
    sender_name = models.CharField(max_length=100, blank=True, null=True)
    sender_mobile = models.CharField(max_length=100, blank=True, null=True)
    sender_address = models.CharField(max_length=100, blank=True, null=True)
    sender_GST = models.CharField(max_length=100, blank=True, null=True)
    receiver_name = models.CharField(max_length=100, blank=True, null=True)
    receiver_mobile = models.CharField(max_length=100, blank=True, null=True)
    receiver_address = models.CharField(max_length=100, blank=True, null=True)
    receiver_GST = models.CharField(max_length=100, blank=True, null=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    gc_date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)


class LCM(models.Model):
    consignment = models.ForeignKey(AddConsignment, on_delete=models.CASCADE,null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    location = models.CharField(max_length=255)
    vehicle_no = models.CharField(max_length=50,null=True)
    driver_name = models.CharField(max_length=100, blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    labour = models.CharField(max_length=100, blank=True, null=True)
    lcm_no = models.CharField(max_length=50, null=True)
    branch = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    branchemail = models.CharField(max_length=255, null=True)
    # Fields for GC/GCC details
    track_id = models.CharField(max_length=50, blank=True, null=True)
    sender_name = models.CharField(max_length=100, blank=True, null=True)
    sender_mobile = models.CharField(max_length=100, blank=True, null=True)
    sender_address = models.CharField(max_length=100, blank=True, null=True)
    sender_GST = models.CharField(max_length=100, blank=True, null=True)
    receiver_name = models.CharField(max_length=100, blank=True, null=True)
    receiver_mobile = models.CharField(max_length=100, blank=True, null=True)
    receiver_address = models.CharField(max_length=100, blank=True, null=True)
    receiver_GST = models.CharField(max_length=100, blank=True, null=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    gc_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.lcm_no} - {self.location}"

