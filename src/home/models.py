from django.db import models
import json
from cryptography.fernet import Fernet

key = b'SVxo6F83ZykoPetuVRswTOoaP-TxY2r-6AQyiX7gveg='
f = Fernet(key)


class Students(models.Model):
    _id = models.AutoField(primary_key=True)
    id = models.IntegerField()
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    University = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    Major = models.CharField(max_length=50)
    EntryYear = models.CharField(max_length=50)
    DateOfBirth = models.CharField(max_length=50)
    SSN = models.BinaryField()
    FatherName = models.CharField(max_length=50)
    CellularPhoneNumber = models.CharField(max_length=50)
    FatherCellularPhoneNumber = models.CharField(max_length=50)
    MotherCellularPhoneNumber = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    DebitCardNumber = models.BinaryField()
    Username = models.BinaryField()
    Password = models.BinaryField()
    PassedCourses = models.CharField(max_length=20000)
    CurrentCourses = models.CharField(max_length=20000)
    UndergraduateCourses = models.CharField(max_length=20000)
    Study = models.CharField(max_length=50)
    Image = models.CharField(max_length=1000)
    Email = models.CharField(max_length=100)

    class Meta:
        db_table = "Students"

    def __str__(self):
        return str(self.FirstName)

    def spc(self, x):
        self.PassedCourses += json.dumps(x)

    def scc(self, x):
        self.CurrentCourses += json.dumps(x)

    def suc(self, x):
        self.UneducatedCourses += json.dumps(x)

    def username(self):
        return f.decrypt(self.Username).decode()


class Courses(models.Model):
    _id = models.AutoField(primary_key=True)
    id = models.IntegerField()
    Course = models.CharField(max_length=100)
    Teacher = models.CharField(max_length=100)
    Date = models.CharField(max_length=100)
    ClassNumber = models.IntegerField()
    EnrollmentCapacity = models.IntegerField()
    Final = models.CharField(max_length=50)

    class Meta:
        db_table = "Courses"


class Semester(models.Model):
    _id = models.AutoField(primary_key=True)
    semester1 = models.CharField(max_length=20000)
    semester2 = models.CharField(max_length=20000)
    semester3 = models.CharField(max_length=20000)
    semester4 = models.CharField(max_length=20000)
    semester5 = models.CharField(max_length=20000)
    semester6 = models.CharField(max_length=20000)
    semester7 = models.CharField(max_length=20000)
    semester8 = models.CharField(max_length=20000)

    class Meta:
        db_table = "Semester"


class Update(models.Model):
    _id = models.AutoField(primary_key=True)
    update = models.CharField(max_length=50000)

    class Meta:
        db_table = "Update"
